import pickle

from twisted.internet.protocol import ReconnectingClientFactory

from pyutils.kv_utils.base import BaseApp
from pyutils.services.enums.protocol_enum import ClientEvents, MessageTypes
from pyutils.services.protocols.main_protocol import MainProtocol


class SpaceProtocol(MainProtocol):
    factory: 'Space'

    def __init__(self):
        super(SpaceProtocol, self).__init__()

    def connectionMade(self):
        self.factory.app.connections[self.prefix] = self
        self.send_data(key=MessageTypes.Event, event=ClientEvents.Connection)

    def on_new_message(self, data):
        print(data)


class Space(ReconnectingClientFactory):
    protocol = SpaceProtocol
    app: BaseApp

    def __init__(self, app: BaseApp):
        super(Space, self).__init__()
        self.app = app
