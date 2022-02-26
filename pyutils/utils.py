import threading


lock = threading.Lock()


def start_new_thread(function):
    """Декоратор для создания потока"""

    def decorator(*args, **kwargs):
        t = threading.Thread(target=function, args=args, kwargs=kwargs)
        t.name = function.__name__
        t.start()

    return decorator
