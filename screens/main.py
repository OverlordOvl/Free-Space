from abc import ABC
from typing import Union

from screens.screen_manager import InitScreen


class Main(InitScreen):
    __metaclass__ = ABC

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)

    def on_kv_post(self, base_widget):
        pass

    def check_invite_code(self):
        if not self.invite_code:
            self.manager.current = 'SelectServer'

    @property
    def invite_code(self) -> str | None:
        return self.settings.primary_server
