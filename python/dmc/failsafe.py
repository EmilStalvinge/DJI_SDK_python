# pylint: disable=E1101,logging-not-lazy
"""Module failsafe defines the failsafe functionality triggered on
drone or pilot disconnect"""
import time
import logging

from dmc.proto.action.action_pb2 import Payload as Action

DEFAULT_CONFIG = [
    {"type": Action.LOITER, "after": 10},
    {"type": Action.LAND, "after": 20},
]

class Failsafe(object):
    """class Failsafe manages failsafe functionality for dmc.Client objetcs.

    The client is responsible for triggering updates on the failsafe object while the failsafe
    emits events corresponding to disconnect duration and failsafe config.

    Two failsafe timers are held; one for server disconnect and one for pilot disconnect.

    Args:
        client (dmc.Client): reference to corresponding client
        config (list of dict of action.Payload.Type : duration (seconds)): current failsafe config
    """
    def __init__(self, client, config=None):
        self.client = client
        self.config = config if config is not None else DEFAULT_CONFIG
        self._server_failsafe = None
        self._pilot_failsafe = None
        self._logger = logging.getLogger("dmc")

    def trigger(self, key):
        """trigger is called when a new thread wants to trigger a failsafe.
        If the failsafe is not currently active (no other threads have called trigger without
        calling clear) the failsafe timestamp is set to the current time

        Args:
            key (string): 'SERVER' or 'PILOT', chooses which disconnect timer to trigger
        """
        if key == "SERVER" and self._server_failsafe is None:
            self._server_failsafe = time.time()
        elif key == "PILOT" and self._pilot_failsafe is None:
            self._pilot_failsafe = time.time()

    def clear(self, key):
        """clear is called when a thread no longer wants to trigger failsafe events

        Args:
            key (string): 'SERVER' or 'PILOT', chooses which disconnect timer to clear
        """
        if key == "SERVER":
            self._server_failsafe = None
        elif key == "PILOT":
            self._pilot_failsafe = None

    def update(self):
        """update is called when a thread wants to emit actions if any failsafe timer is active.
        Depending on the current config, actions might be emitted from the client object

        If both timers are active, the earliest triggered one is chosen.
        """
        has_server = self._server_failsafe is not None
        has_pilot = self._pilot_failsafe is not None
        if has_server and has_pilot:
            self._emit(min(self._server_failsafe, self._pilot_failsafe))
        elif has_server:
            self._emit(self._server_failsafe)
        elif has_pilot:
            self._emit(self._pilot_failsafe)

    def _emit(self, start_time):
        diff = time.time() - start_time
        for i, item in enumerate(self.config):
            if diff < item["after"]:
                self._logger.info("returning, no action")
                return
            if i < len(self.config)-1:
                self._logger.info("returning, next action")
                if diff > self.config[i+1]["after"]:
                    continue
            if self.client.status.mode == "AUTO" or self.client.status.mode == "GUIDED":
                action = Action(type=item["type"])
                self._logger.info("failsafe emitting: %s" % action)
                self.client.emit("action", action)
            return
