import os
from pathlib import Path

from dotenv import load_dotenv
from kivy.storage.jsonstore import JsonStore


load_dotenv()

from kivy.app import App
from kivy.utils import platform


FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)))
ROOT_PATH = str(Path(FILE_PATH).parent)

if platform == 'android':
    from jnius import autoclass
    from android.permissions import request_permissions, Permission


    request_permissions(
        [
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_EXTERNAL_STORAGE,
        ]
    )


class AppStorage:

    def __init__(self):
        self.json_storage = JsonStore('FreeSpaceStorage.json')

        self.path = App.get_running_app().user_data_dir
        self.media_path = os.path.join(self.path, 'media')

        self.path_collections = {
            'media': self.media_path,
            'audio': os.path.join(self.media_path, 'audio'),
            'photo': os.path.join(self.media_path, 'photo'),
            'video': os.path.join(self.media_path, 'video'),
            'other': os.path.join(self.media_path, 'other'),
            'app_data': os.path.join(self.path, 'app_data'),
            'ssl': os.path.join(self.path, 'ssl'),
        }
        self.init_directories()

    def init_directories(self):
        for directory in self.path_collections:
            self.create_directory(self.path_collections[directory])

    def create_directory(self, path):
        """Make media directory in root path"""
        directory_path = os.path.join(self.path, path)
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

    def add_audio_file(self, path, raw_file):
        with open(f'{self.path}/{path}', 'w') as f:
            f.write(raw_file)

    def add_file(self, path, raw_file):
        with open(f'{self.path}/{path}', 'w') as f:
            f.write(raw_file)

    def server(self) -> dict:
        if self.json_storage.exists('server'):
            return self.json_storage.get('server')
        else:
            self.json_storage.put('server')
            return self.json_storage.get('server')

    @property
    def primary_server(self):
        return self.server().get('primary_server') if self.server().get('primary_server') else {
            'ip': os.getenv('PRIMARY_SERVER_IP'),
            'port': int(os.getenv('PRIMARY_SERVER_PORT'))
        }

    def get_auth_data(self, server):
        pass

    @property
    def current_server(self):
        return self.server().get('current_server')

    @current_server.setter
    def current_server(self, value):
        self.server().update({'current_server': value})
        self.json_storage.put('server', **self.server())

    def add_server(self, name, key, port, ip):
        self.server().update({name: {'invite_code': key, 'port': port, 'key': key, 'ip': ip}})
        self.json_storage.put('server', **self.server())

    def set_json(self, key, value):
        self.json_storage.store_put(key, value)
