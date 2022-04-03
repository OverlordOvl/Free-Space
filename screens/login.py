from abc import ABC

from screens.screen_manager import InitScreen


class Login(InitScreen):
    __metaclass__ = ABC

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)

    def validate(self):
        login_widget = self.ids['login']
        password_widget = self.ids['password']
        login = login_widget.text
        password = password_widget.text

