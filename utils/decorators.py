from functools import wraps
from typing import Any, Callable, Dict, Union

from flask import abort, current_app, request

from errors import errors as err


def debug_only(f):
    """
    A decorator that only allows the decorated function to be called if the Flask app is in debug mode.

    If the app is not in debug mode, a 404 error will be raised.
    """

    @wraps(f)
    def wrapped(**kwargs):
        if not current_app.debug:
            abort(404)

        return f(**kwargs)

    return wrapped


def json_only(ignore: list[str] = []):
    """
    A decorator that checks if the request contains JSON data and passes it to the decorated function.

    Args:
        ignore (list[str], optional): A list of HTTP methods to ignore the JSON check for. Defaults to [].

    Returns:
        Callable[..., Union[Dict[str, Any], Any]]: The decorated function.
    """

    def json(f: Callable[..., Union[Dict[str, Any], Any]]):
        @wraps(f)
        def wrapped(*args, **kwargs):
            # Skip JSON check if request method is in ignore_request_methods
            if request.method in ignore:
                return f({}, *args, **kwargs)

            if not request.is_json:
                return err.NoJsonError()
            try:
                data = request.get_json(force=True)
                if data is None:
                    raise ValueError  # raise an exception if parsed JSON is None
            except (
                Exception
            ):  # you can replace this with a more specific exception if needed
                return err.NoJsonError()
            return f(data, *args, **kwargs)

        return wrapped

    return json
