import functools
import logging
import warnings
from typing import Optional, Callable, TypeVar, ParamSpec

import requests

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

P = ParamSpec('P')
T = TypeVar('T')


def retry(times, exceptions):
    """
    Retry Decorator
    Retries the wrapped function/method `times` times if the exceptions listed
    in ``exceptions`` are thrown
    :param exceptions:
    :param times: The number of times to repeat the wrapped function/method
    :type times: Int
    :param Exceptions: Lists of exceptions that trigger a retry attempt
    :type Exceptions: Tuple of Exceptions
    """

    def actual_decorator(func):
        def decorated(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    print(
                        'Exception thrown when attempting to run %s, attempt '
                        '%d of %d' % (func, attempt, times)
                    )
                    attempt += 1
            return func(*args, **kwargs)

        return decorated

    return actual_decorator


def deprecated(instead: Optional[str] = None) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def actual_decorator(func: Callable[P, T]) -> Callable[P, T]:
        @functools.wraps(func)
        def decorated(*args: P.args, **kwargs: P.kwargs) -> T:
            warnings.simplefilter('always', DeprecationWarning)  # turn off filter
            if instead:
                fmt = "{0.__name__} is deprecated, use {1} instead."
            else:
                fmt = '{0.__name__} is deprecated.'

            warnings.warn(fmt.format(func, instead), stacklevel=3, category=DeprecationWarning)
            warnings.simplefilter('default', DeprecationWarning)  # reset filter
            return func(*args, **kwargs)

        return decorated

    return actual_decorator


def add_logging(f: Callable[P, T]) -> Callable[P, T]:
    """A type-safe decorator to add logging to a function."""

    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info(f'{f.__name__} was called')
        return f(*args, **kwargs)

    return inner


def catch_exception(function):
    def decorator(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            raise e

    return decorator


def download_image(url: str, file_name: str) -> bool:
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
            return True
    warnings.warn("Failed to download image")
    return False


if __name__ == "__main__":
    @add_logging
    def add_two(x: float, y: float) -> float:
        """Add two numbers together."""
        return x + y


    add_two(1.0, 2.0)
