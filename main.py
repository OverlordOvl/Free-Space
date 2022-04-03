import os

from kivy.graphics import Rectangle
from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, WipeTransition
from kivymd.theming import ThemeManager

from pyutils.kv_utils.base import BaseApp
from pyutils.services.space_protocol import Space
from screens import __ALL_SCREENS__


Builder.load_string(open("kv/client.kv", encoding="utf-8").read())


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


class FreeSpaceApp(BaseApp):

    def __init__(self):
        super(FreeSpaceApp, self).__init__()
        self.theme_cls = ThemeManager()
        self.title = "Free Space"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        # self.icon = "Image/main.jpeg"
        return self.initialize()

    def initialize(self):
        self.connect_to_server('localhost', 8000, Space)
        return SM()


FreeSpaceApp().run()
