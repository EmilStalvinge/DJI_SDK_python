# pylint: disable=E1101,logging-not-lazy
"""Module client implements the class to create a Client object communicating with
drone mission control

Attributes:
    PRIO_LIST (list of str): telemetry to send with priority (over gRPC connection)
    NORMAL_LIST (lisg of str): telemetry to send to log only

    DMC_URI (str): uri of dronemissioncontrol server
    DMC_ANIP_URI (str): uri of anip authentication server
    DMC_SESSION_URI (str): uri of session gRPC endpoint
    DMC_INSECURE (int): set to use insecure connection (no ssl)

Todo:
    * Split up Client class into more separate classes/apis (queues/event list)
    * Fix failsafe
    * Write tests
"""

import logging
import threading
import time
import json
import os
from Queue import Queue, Empty

from jose import jwk
from jose.utils import base64url_decode
from pyee import EventEmitter
import requests
from google.protobuf import any_pb2
import grpc

from dmc.proto.services import session_pb2_grpc
from dmc.proto.mission.mission_pb2 import (Home, Payload as Mission)
from dmc.proto.status.status_pb2 import Payload as Status
from dmc.proto.telemetry.telemetry_pb2 import (
    Position,
    Heading,
    Battery,
    Connection,
    Velocity,
    Payload as Telemetry,
    LogPayload as TelemetryLog)
from dmc.proto.action.action_pb2 import Payload as Action
from .failsafe import Failsafe

PRIO_LIST = [Position.DESCRIPTOR.name, Heading.DESCRIPTOR.name, Velocity.DESCRIPTOR.name]
NORMAL_LIST = [Battery.DESCRIPTOR.name, Connection.DESCRIPTOR.name]

DMC_URI = os.getenv("DMC_URI", "api.dronemissioncontrol.com")
DMC_ANIP_URI = os.getenv("DMC_ANIP_URI")
DMC_SESSION_URI = os.getenv("DMC_SESSION_URI", "drone.dronemissioncontrol.com:80")
DMC_INSECURE = os.getenv("DMC_INSECURE")

def get_name(msg):
    """get_name is a helper to return the name of a
    protobuf message

    Args:
        param1 (protobuf message): the message to get name of
    Returns:
        string: the message name
    """
    return msg.DESCRIPTOR.name

class AuthException(Exception):
    """AuthException is raised when the client fails to
    authenticate with dmc"""
    pass

class Client(EventEmitter):
    """Client communicates with drone mission control.

    To listen for messages from pilots, attach a callback.

    Example:
        @client.on('event_name')
        def callback_fn(msg):
            ...

    Supported events are 'set_mission', 'start_mission' and 'action'.

    Args:
        drone_id (string): id of the drone to connect as
        password (string): password of the drone to connect as
    """
    # pylint: disable=too-many-instance-attributes
    _status = Status()
    _mission = Mission(reached=-1)
    _action = None
    _msg_queue = Queue()
    _telemetry_queue = Queue()
    _prio_queue = Queue()
    _mission_lock = threading.Lock()
    _event_history = ['DEFAULT']*5
    _logger = logging.getLogger("dmc")
    _tmp_speed = []
    def __init__(self,
                 drone_id,
                 password):
        super(Client, self).__init__()
        self.drone_id = str(drone_id)
        self.password = str(password)
        self._failsafe = Failsafe(client=self)

    @property
    def mission(self):
        "mission.Payload: returns currently set mission"
        return self._mission

    @property
    def status(self):
        "status.Payload: returns currently set status"
        return self._status

    @property
    def action(self):
        "action.Payload: returns currently set action"
        return self._action

    def _get_token(self):
        # Fetch key from server
        http_protocol = "http" if DMC_INSECURE else "https"
        self._logger.info(
            "attempting to authenticate on %s://%s" % (http_protocol, DMC_URI)
        )
        key = requests.get('{}://{}/drone/keys.json'.format(http_protocol, DMC_URI))
        if key.status_code >= 299:
            self._logger.error("could not fetch keys, server error")
            raise AuthException('could not access keys: {}'.format(key.status_code))
        key = key.json()

        # Authenticate
        anip_uri = DMC_ANIP_URI or "{}/drone/auth".format(DMC_URI)
        self._logger.info("fetching token from %s" % anip_uri)
        ret = requests.post("{}://{}".format(http_protocol, anip_uri),
                            json={
                                'id': self.drone_id,
                                'password': self.password
                            })
        if ret.status_code >= 500:
            raise AuthException('could not fetch token, server error')
        elif ret.status_code > 299:
            raise AuthException('unauthorized: {}'.format(ret))

        # Verify recieved token with key from server
        token = ret.json()['token']
        rsa_key = jwk.construct(key)
        message, encoded_sig = token.rsplit('.', 1)
        decoded_sig = base64url_decode(str(encoded_sig))
        if not rsa_key.verify(message, decoded_sig):
            raise AuthException('invalid token')
        payload = message.split('.')[1]
        auth = json.loads(base64url_decode(str(payload)))
        return token, auth

    def _add_event(self, event):
        self._event_history = [event] + self._event_history[:-1]

    def get_event(self, idx):
        """get_event returns the type of up to 5 previous events

        events are either "ACTION" or "MISSION" depending on what
        event was sent from the pilot

        Args:
            idx (int): index of the event, 0 for most recent
        Returns:
            string: type of the event
        """
        try:
            return self._event_history[idx]
        except IndexError:
            return "ERROR"

    def _handle_message(self, msg):
        self._failsafe.clear("PILOT")
        if msg.Is(Mission.DESCRIPTOR):
            mission = Mission()
            msg.Unpack(mission)
            self._add_event("MISSION")
            if mission.cmd == Mission.SET:
                self._tmp_speed = [wp.speed for wp in mission.waypoints]
                self.emit("set_mission", mission)
            elif mission.cmd == Mission.START:
                self.emit("start_mission", mission)
        elif msg.Is(Action.DESCRIPTOR):
            action = Action()
            msg.Unpack(action)
            if action.type == Action.FAILSAFE:
                self._failsafe.trigger("PILOT")
            else:
                self._add_event("ACTION")
                self.emit("action", action)

    def _flush_telemetry_queue(self, queue, log=False):
        if log:
            msg = TelemetryLog()
        else:
            msg = Telemetry()
        try:
            while True:
                data = queue.get_nowait()
                typ = get_name(data)
                if typ == get_name(Position):
                    msg.position.CopyFrom(data)
                elif typ == get_name(Heading):
                    msg.heading.CopyFrom(data)
                elif typ == get_name(Connection):
                    msg.connection.CopyFrom(data)
                elif typ == get_name(Battery):
                    msg.battery.CopyFrom(data)
                elif typ == get_name(Velocity):
                    msg.velocity.CopyFrom(data)
        except Empty:
            pass
        raw = any_pb2.Any()
        raw.Pack(msg)
        self._logger.debug("_send_telemetry_queue: sending message: %s" % msg)
        return raw

    def _flush_message_queue(self):
        try:
            msg = self._msg_queue.get_nowait()
            raw = any_pb2.Any()
            raw.Pack(msg)
            self._logger.debug("_send_message_queue: sending message: %s" % msg)
            return raw
        except Empty:
            pass

    def _gen_msg(self, run_event):
        counter = 1
        while run_event.is_set():
            time.sleep(0.2)
            normal_rate = 25 if self._status.code == Status.ACTIVE else 75
            if self._status.code == Status.ACTIVE or counter % normal_rate == 0:
                yield self._flush_telemetry_queue(self._prio_queue)
            if counter % normal_rate == 0:
                yield self._flush_telemetry_queue(self._telemetry_queue, log=True)
            msg = self._flush_message_queue()
            if msg is not None:
                yield msg
            counter += 1
            self._failsafe.update()

    def spin(self):
        """spin blocks and runs the Client object until interrupted"""
        self._logger.debug("spinning")

        try:
            while True:
                run_event = threading.Event()
                run_event.set()
                try:
                    # fetch token
                    token, auth = self._get_token()
                    self._logger.info("gRPC connecting on %s" % DMC_SESSION_URI)

                    # connect to service
                    channel = grpc.insecure_channel(DMC_SESSION_URI)
                    stub = session_pb2_grpc.SessionStub(channel)
                    recieved = stub.Stream(
                        request_iterator=self._gen_msg(run_event),
                        metadata=[
                            ('orgid', auth['orgId']),
                            ('droneid', auth['id']),
                            ('authorization', token),
                        ]
                    )
                    self._logger.info("gRPC successfully connected")

                    for msg in recieved:
                        self._failsafe.clear("SERVER")
                        self._handle_message(msg)

                except AuthException as err:
                    self._logger.error('could not connect: %s' % err)

                except grpc.RpcError as err:
                    self._logger.error('connection lost: %s' % err)

                finally:
                    self._failsafe.trigger("SERVER")
                    self._failsafe.update()
                    time.sleep(1)
                    run_event.clear()
        except KeyboardInterrupt:
            run_event.clear()

    def set_mission(self, waypoints=None, home=None, reached=None, error=None):
        """set_mission updates the current mission in dronemissioncontrol

        Args:
            waypoints (list of mission.Waypoint): updated waypoints
            home (mission.Home): updated home position
            reached (int): updated reached index
            error (string): error message, None if successful
        """
        with self._mission_lock:
            if waypoints is not None and len(self._tmp_speed) == len(waypoints):
                for i, speed in enumerate(self._tmp_speed):
                    waypoints[i].speed = speed

            diff = waypoints is not None and \
                    (len(waypoints) != len(self._mission.waypoints) or len(waypoints) == 0)
            if not diff and waypoints is not None:
                for idx, waypoint in enumerate(waypoints):
                    if waypoint != self._mission.waypoints[idx]:
                        diff = True
                        break
            if diff:
                self._mission.ClearField("waypoints")
                self._mission.waypoints.extend(waypoints)

            if home is not None and home != self._mission.home:
                diff = True
                self._mission.home.CopyFrom(home)

            if reached is not None and reached != self._mission.reached:
                diff = True
                self._mission.reached = reached

            if error is not None and error != self._mission.errMsg:
                diff = True
                self._mission.errMsg = error

            self._mission.cmd = Mission.SET_SUCCESS if error is None else Mission.SET_FAIL
            if diff or error:
                self._logger.info("set_mission: setting mission: %s" % self._mission)
                self._msg_queue.put(self._mission)

    def set_home(self, home):
        """set_home updates the current home position in dronemissioncontrol

        Args:
            home (mission.Home): updated home position
        """
        self._logger.info("setting home position: %s" % home)
        with self._mission_lock:
            if not isinstance(home, Home):
                pass
            self._mission.home.CopyFrom(home)
            msg = Mission(cmd=Mission.SET_HOME)
            msg.home.CopyFrom(home)
            self._msg_queue.put(msg)

    def set_reached(self, reached):
        """set_reached updates reached index in dronemissioncontrol

        If final waypoint reached, the mission state is set to FINISHED

        Args:
            reached (int): updated reached index
        """
        with self._mission_lock:
            self._mission.reached = reached
            msg = Mission(cmd=Mission.REACHED, reached=reached)
            self._logger.info("reached %d" % reached)
            self._msg_queue.put(msg)

            if self._mission.waypoints and \
                reached == len(self._mission.waypoints)-1:
                self._mission.cmd = Mission.FINISHED
                self._logger.info("mission finished")
                self._msg_queue.put(Mission(cmd=Mission.FINISHED))


    def set_started(self, success, error=None):
        """set_started updates the result of a mission start attempt

        Args:
            success (bool): True if the mission was successfully started
            error (string): error message, None if successful
        """
        with self._mission_lock:
            if not success and error is None:
                error = "Start command failed"

            self._mission.cmd = Mission.START_SUCCESS if success else Mission.START_FAIL
            if error is not None:
                self._mission.errMsg = error

            self._logger.info("started: %s with error: %s" % (success, error))
            self._msg_queue.put(Mission(cmd=self._mission.cmd))

    def set_status(self, status):
        """set_status updates the drone status in dronemissioncontrol

        Args:
            status (status.Payload): updated status
        """
        if not isinstance(status, Status):
            pass

        diff = False
        if status.code != self._status.code:
            diff = True
            self._status.code = status.code

        if status.arm != self._status.arm:
            diff = True
            self._status.arm = status.arm

        if status.errMsg != self._status.errMsg:
            diff = True
            self._status.errMsg = status.errMsg

        if status.mode != self._status.mode:
            diff = True
            self._status.mode = status.mode

        if diff:
            self._logger.info("set status %s" % status)
            self._msg_queue.put(self._status)

    def set_action(self, action, error=None):
        """set_action updates the current action in dronemissioncontrol

        Args:
            action (action.Payload): updated action
            error (string): error message, None if successful
        """
        self._logger.info("set action: %s with error: %s" % (action, error))
        if not isinstance(action, Action):
            pass

        if error is not None:
            action.status = Action.FAIL
            action.errMsg = error
        else:
            action.status = Action.SUCCESS
        self._action = action

        self._msg_queue.put(self._action)

    def send_telemetry(self, msg):
        """send_telemetry sends drone telemetry to dronemissioncontrol

        Args:
            telemetry (any telemetry type): the telemetry object to send, any
            message in telemetry is valid
        """
        name = msg.DESCRIPTOR.name
        if name not in PRIO_LIST + NORMAL_LIST:
            pass
        prio = name in PRIO_LIST
        self._telemetry_queue.put(msg)
        if prio:
            self._prio_queue.put(msg)

    def send_log(self, log):
        """send_log sends an autopilot log message to dronemissioncontrol

        Args:
            log (log.Payload): autopilot log message
        """
        self._msg_queue.put(log)
