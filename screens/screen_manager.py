from kivy.app import App
from kivy.utils import platform
from kivy.storage.jsonstore import JsonStore
from dotenv import load_dotenv

from kivymd.uix.screen import MDScreen
from twisted.internet import reactor

from pyutils.kv_utils.base import BaseApp
from pyutils.os.storage import AppStorage
from pyutils.session.client import SessionFactory
from pyutils.session.ssl import CRTFactory


load_dotenv()

if platform == 'android':
    pass

__ALL_SCREENS__ = {}


class InitScreen(MDScreen):
    """
    Данный класс является сборщиком всех собвстенных наследоанных,
    которым требуется модуль kivymd.uix.screen.MDScreen для корректной
    работы сборщика kivy
    """
    app: BaseApp
    storage: AppStorage
    connected_to_primary_server = False
    initialized = False

    def __init_subclass__(cls, **kwargs):
        __ALL_SCREENS__.update({cls.__name__: cls})
        super(InitScreen, cls).__init_subclass__(**kwargs)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.settings = self.app.settings
        self.app._screen = self

    @property
    def external_storage_path(self):
        return self.app.storage.path

    @property
    def json_storage(self):
        return self.app.storage.json_storage

    def connect_to_primary_server(self):
        server = self.app.storage.primary_server
        reactor.connectTCP(
            server['ip'],
            server['port'],
            SessionFactory(self),
        )
        self.connected_to_primary_server = True

    def connect_to_server_ssl(self):
        reactor.connectSSL(
            self.app.settings.server,
            self.app.settings.factories["MainFactory"]["port"],
            SessionFactory(self),
            CRTFactory(self.storage.ssl_keys_path),
        )
