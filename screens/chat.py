from abc import ABC
from typing import Union

from pyutils.services.enums.protocol_enum import MessageTypes
from screens.screen_manager import InitScreen


class Chat(InitScreen):
    __metaclass__ = ABC

    def __init__(self, **kwargs):
        super(Chat, self).__init__(**kwargs)

    def send_message(self):
        text = self.ids['input'].text
        self.app.connections['space'].send_data(MessageTypes.Message, data=text)
        self.ids['input'].text = ""
