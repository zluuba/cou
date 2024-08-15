from functools import wraps


def suppress_traceback(func):
    """
    Decorator that catches any exceptions raised by the wrapped function
    and prints a simplified error message without displaying the traceback.

    Args:
        func (function): The function to be wrapped.

    Returns:
        function: The wrapped function with error handling.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(error)

    return wrapper
