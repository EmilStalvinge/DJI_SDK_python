# pylint: disable=E1101,logging-not-lazy
import os
from Queue import Queue, Empty
import threading
import time

from google.protobuf import any_pb2
from pyee import EventEmitter
import grpc

from dmc.proto.services import launcher_pb2_grpc
from dmc.proto.launcher.launcher_pb2 import Payload, Command
from dmc.proto.telemetry.telemetry_pb2 import Position, Payload as Telemetry

DMC_LAUNCHER_URI = os.getenv("DMC_LAUNCHER_URI", "35.228.236.231:80")

def get_name(msg):
    """get_name is a helper to return the name of a
    protobuf message

    Args:
        param1 (protobuf message): the message to get name of
    Returns:
        string: the message name
    """
    return msg.DESCRIPTOR.name

class LauncherClient(EventEmitter):
    _state = Payload(mode=Payload.INACTIVE)
    _command = Command()
    _msg_queue = Queue()
    def __init__(self, launcher_id, password):
        super(LauncherClient, self).__init__()
        self.launcher_id = str(launcher_id)
        self.password = str(password)

    @property
    def position(self):
        return self._state.position

    @property
    def mode(self):
        return self._state.mode

    @property
    def command(self):
        return self._command

    def _handle_message(self, msg):
        if msg.Is(Command.DESCRIPTOR):
            cmd = Command()
            msg.Unpack(cmd)
            self._command = cmd
            self.emit("command", cmd)

    def _flush_queue(self):
        try:
            msg = self._msg_queue.get_nowait()
            raw = any_pb2.Any()
            raw.Pack(msg)
            return raw
        except Empty:
            pass

    def _gen_msg(self, run_event):
        while run_event.is_set():
            msg = self._flush_queue()
            if msg is not None:
                print(msg)
                yield msg
            time.sleep(1)
            
    def spin(self):
        print('spinning')
        try:
            while True:
                try:
                    run_event = threading.Event()
                    run_event.set()
                    print('connecting on: ', DMC_LAUNCHER_URI)
                    channel = grpc.insecure_channel(DMC_LAUNCHER_URI)
                    print('created channel')
                    stub = launcher_pb2_grpc.LauncherStub(channel)
                    recieved = stub.Stream(
                        request_iterator=self._gen_msg(run_event),
                        metadata=[
                            ('id', self.launcher_id),
                            ('password', self.password),
                        ]
                    )
                    for msg in recieved:
                        print(msg)
                        self._handle_message(msg)

                except grpc.RpcError as err:
                    print('grpc error: ', err)

                finally:
                    time.sleep(1)
                    run_event.clear()
        except KeyboardInterrupt:
            print('interrupted')
            run_event.clear()

    def set_position(self, position):
        print(position)
        if get_name(position) != get_name(Position):
            return
        
        self._state.position.CopyFrom(position)
        self._msg_queue.put(self._state)
        print(self._state)

    def set_mode(self, mode):
        if mode not in Payload.Mode.values():
            return
        
        self._state.mode = mode
        self._msg_queue.put(self._state)
