from kivy.uix.screenmanager import ScreenManager, WipeTransition
from kivymd.app import MDApp
from kivymd.theming import ThemeManager

from pyutils.os.storage import AppStorage
from pyutils.session.client import SessionProtocol


class SM(ScreenManager):
    """Window change manager"""

    def __init__(self, **kwargs):
        super(SM, self).__init__(**kwargs)
        self.transition = WipeTransition(duration=0.4)

    @staticmethod
    def hook_keyboard(self, window, key, *args, **kwargs):
        del args, kwargs
        if key == 27:
            self.current = self.previous()


class BaseApp(MDApp):
    storage: AppStorage

    def __init__(self, **kwargs):
        super().__init__()
        self.settings = Settings(self)
        self.api = API(self)

    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Dark"
        return SM()

    def on_start(self):
        self.storage = AppStorage()


class Settings:

    def __init__(self, app: BaseApp):
        self.app = app

    @property
    def primary_server(self):
        return self.app.storage.current_server

    @primary_server.setter
    def primary_server(self, value):
        self.app.storage.current_server = value


class API:

    def __init__(self, app: BaseApp, session: SessionProtocol = None):
        self.app = app
        self.session = session

    def send_invite_code(self, code):
        self.session.sendString(code)
