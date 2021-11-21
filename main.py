import os
from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, WipeTransition
from kivymd.theming import ThemeManager


def get_kv():
    with open("kv/client.kv", encoding="utf-8") as f:
        return Builder.load_string(f.read())


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


class MainApp(MDApp):

    def build(self):
        self.title = "Free Space"
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Dark"
        # self.icon = "Image/main.jpeg"
        return self.initialize()

    def initialize(self):
        return SM()


MainApp().run()
