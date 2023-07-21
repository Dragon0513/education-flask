from functools import wraps

from flask import abort, current_app


def debug_only(f):
    @wraps(f)
    def wrapped(**kwargs):
        if not current_app.debug:
            abort(404)

        return f(**kwargs)

    return wrapped
