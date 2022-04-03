from pyutils.services.enums.enum_type import BaseEnum
from pyutils.services.protocols.message_protocol import MessageProtocol


class EventProtocol(MessageProtocol):
    callbacks = {}

    def __init__(self, *args, **kwargs):
        super(EventProtocol, self).__init__(*args, **kwargs)
        self.register_events()

    def register_events(self):
        ...

    def dataReceived(self, data: bytes):
        data = super(EventProtocol, self).dataReceived(data)

        if data["endpoint"] in self.callbacks:
            self.callbacks[data["endpoint"]]()

    @classmethod
    def on(cls, event: BaseEnum, callback: callable):
        cls.callbacks[event] = callback
