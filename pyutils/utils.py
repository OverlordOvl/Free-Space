import threading


lock = threading.Lock()


def start_new_thread(function):
    """Декоратор для создания потока"""

    def decorator(*args, **kwargs):
        t = threading.Thread(target=function, args=args, kwargs=kwargs)
        t.name = function.__name__
        t.start()

    return decorator


def snake_to_camel(string: str):
    return "".join(word.title() for word in string.split("_"))
