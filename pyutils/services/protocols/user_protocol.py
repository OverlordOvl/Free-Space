from pyutils.services.enums.protocol_enum import ClientEvents
from pyutils.services.protocols.context_protocol import ContextProtocol
from pyutils.services.protocols.event_protocol import EventProtocol
from pyutils.services import space_protocol


class UserProtocol(EventProtocol, ContextProtocol):
    user_id: int
    token: str
    factory: 'space_protocol.Space'

    def __init__(self):
        super(UserProtocol, self).__init__()

    def register_events(self):
        self.on(ClientEvents.AuthenticationRequest, self.send_auth_data)

    def send_auth_data(self):
        self.factory.app.settings
