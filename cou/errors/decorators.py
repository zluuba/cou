from functools import wraps

from cou.errors.exceptions import FileNotReadable, UnexpectedError


def suppress_traceback(func):
    """
    Decorator that catches any exceptions raised by the wrapped function
    and prints a simplified error message without displaying the traceback.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(error)

    return wrapper


def catch_file_errors(func):
    """
    Decorator that catches any file-related errors and appends them
    to the _errors list of the File instance.
    """

    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        try:
            return await func(self, *args, **kwargs)
        except (OSError, IOError):
            self.errors.append(FileNotReadable(self.path))
            return 0
        except Exception as error:
            self.errors.append(UnexpectedError(error))
            return 0
        finally:
            if '_progress_bar' in kwargs:
                kwargs['_progress_bar'].update(1)

    return wrapper
