from kivy.clock import Clock


def timer_single(function, timer=0, *args, **kwargs):
    Clock.schedule_once(lambda dt: function(*args, **kwargs), timer)
