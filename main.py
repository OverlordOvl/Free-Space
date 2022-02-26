import webbrowser

from kivy.support import install_twisted_reactor

from kivy.lang import Builder
from pyutils.kv_utils.base import BaseApp
# from pyutils.session import client


install_twisted_reactor()

from screens import __ALL_SCREENS__


class FreeSpaceApp(BaseApp):
    title = 'FreeSpace'

    @staticmethod
    def open_github():
        webbrowser.open('https://github.com/OverlordOvl/Free-Space')


if __name__ == '__main__':
    Builder.load_string(open("kv/client.kv", encoding="utf-8").read())
    FreeSpaceApp().run()
