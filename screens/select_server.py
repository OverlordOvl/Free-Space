from typing import Union

from pyutils.kv_utils.timer import timer_single
from screens.screen_manager import InitScreen


class SelectServer(InitScreen):

    def __init__(self, **kwargs):
        super(SelectServer, self).__init__(**kwargs)

    @property
    def invite_code(self) -> Union[str, None]:
        return self.json_storage.get('invite_code') if self.json_storage.exists('invite_code') else None

    def set_invite_code(self):
        timer_single(self.connect_to_primary_server)
        invite_code = self.ids['invite_code'].text
        if not invite_code:
            self.ids['invite_code'].focus = True
            self.ids['invite_code'].focus = False
            return
        self.app.api.send_invite_code()
