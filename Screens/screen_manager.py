
from kivymd.uix.screen import MDScreen


__ALL_SCREENS__ = {}


class InitScreen(MDScreen):
    """
    Данный класс является сборщиком всех собвстенных наследоанных,
    которым требуется модуль kivymd.uix.screen.MDScreen для корректной
    работы сборщика kivy
    """

    def __init_subclass__(cls, **kwargs):
        __ALL_SCREENS__.update({cls.__name__: cls})

        super(InitScreen, cls).__init_subclass__(**kwargs)
