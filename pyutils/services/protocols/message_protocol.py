import pickle
import _pickle
import traceback

from twisted.internet.protocol import Protocol
from loguru import logger

from pyutils.services.enums.protocol_enum import ClientEvents, MessageTypes


class MessageProtocol(Protocol):

    def dataReceived(self, data: bytes):
        try:
            self.on_new_message(pickle.loads(data))
        except TypeError as e:
            logger.error("".join(traceback.format_tb(e.__traceback__)))
        except _pickle.UnpicklingError as e:
            logger.error("".join(traceback.format_tb(e.__traceback__)))

    def on_new_message(self, data):
        ...

    def send_data(self, key: MessageTypes, data: str | int | float | list | dict = None, event: ClientEvents = None):
        message = pickle.dumps({'key': key, 'event': event, 'data': data})
        self.transport.write(bytes(message))
