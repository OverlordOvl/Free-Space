from abc import ABC

from twisted.internet import protocol
from twisted.internet.protocol import connectionDone
from twisted.protocols.basic import NetstringReceiver

from pyutils.kv_utils.timer import timer_single


class InitializationProtocol(NetstringReceiver, ABC):
    _last_buffer: bytes

    def __init__(self):
        self.first_connection = True
        self.app = self.factory.app
        self.storage = self.app.storage

    def connectionMade(self):
        self.app_storage

    def connectionLost(self, reason=connectionDone):
        self.first_connection = False

    def stringReceived(self, line):
        """Handler for sent data lines. Sends it to the handler."""
        self._buffer += line
        self._last_buffer = line


class SessionProtocol(NetstringReceiver, ABC):
    _last_buffer: bytes

    def __init__(self):
        self.first_connection = True

    def connectionMade(self):
        """Handler for new connections. The connection is placed in a separate thread"""
        if not hasattr(self, 'app'):
            self.app = self.factory.app
            self.app.api.session = self

    def connectionLost(self, reason=connectionDone):
        self.first_connection = False

    def stringReceived(self, line):
        """Handler for sent data lines. Sends it to the handler."""
        self._buffer += line
        self._last_buffer = line


class SessionFactory(protocol.ReconnectingClientFactory):
    protocol = SessionProtocol

    def __init__(self, app):
        self.app = app


class InitializationFactory(protocol.ReconnectingClientFactory):
    protocol = InitializationProtocol

    def __init__(self, app):
        self.app = app
