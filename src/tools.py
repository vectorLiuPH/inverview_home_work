from functools import wraps

from selenium.common import WebDriverException


def element_exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except WebDriverException as e:
            raise Exception('element {0} not found.\n\tException: {1}.'.format(
                args, repr(e)))
        else:
            return result

    return wrapper


def api_exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            raise Exception(repr(e))
        else:
            return result

    return wrapper
