from typing import Union

from kivy.clock import Clock

from pyutils.kv_utils.timer import timer_single
from screens.screen_manager import InitScreen


class Main(InitScreen):

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        timer_single(self.check_invite_code)

    def check_invite_code(self):
        if not self.invite_code:
            self.manager.current = 'SelectServer'

    @property
    def invite_code(self) -> Union[str, None]:
        return self.settings.primary_server
