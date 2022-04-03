import warnings

from twisted.internet.protocol import Protocol

from pyutils.services.protocols.context_protocol import ContextProtocol
from pyutils.services.protocols.event_protocol import EventProtocol
from pyutils.services.protocols.message_protocol import MessageProtocol
from pyutils.services.protocols.user_protocol import UserProtocol
from pyutils.utils import snake_to_camel


class MainProtocol(
    UserProtocol, EventProtocol
):
    ...

    def __init_subclass__(cls, **kwargs):
        if "protocol" not in cls.__name__.lower():
            warnings.warn(
                f'The prefix "Protocol" must be present in the name of the protocol\n'
                f"Hint: you have installed {cls.__name__} but there must be a named {snake_to_camel(cls.__name__ + '_Protocol')}",
                SyntaxWarning,
            )
        cls.prefix = cls.__name__.lower().replace("protocol", "")
