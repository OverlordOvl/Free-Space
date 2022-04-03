from abc import ABC

from screens.screen_manager import InitScreen


class Registration(InitScreen):
    __metaclass__ = ABC

    def __init__(self, **kwargs):
        super(Registration, self).__init__(**kwargs)

    def registration(self):
        pass
