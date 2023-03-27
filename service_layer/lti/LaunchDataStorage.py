"""This module provides a simple storage for LTI launch data. It is used to store the launch data for the LTI launch request with short lived keys. The keys are used to retrieve the launch data. The launch data is stored for 1 minute. After that the key is deleted and the launch data is no longer available."""
from datetime import datetime, timedelta
from typing import Dict
from errors import errors as err

_dict : Dict[str, tuple[str, datetime]] = {}
def set_value(key, value, expiration= 1):
    """Sets the value for the given key. The value is stored for the given expiration time in minutes."""
    # if conflict throw exception
    if key in _dict:
        raise err.KeyAlreadyExistsError(message="Key already exists")

    _dict[key] = (value, datetime.utcnow() + timedelta(minutes=expiration)) # 1 minute expiration for authorization

def get_value(key) -> str | None:
    if key in _dict:
        value, expiration = _dict[key]
        if expiration < datetime.utcnow():
            del _dict[key]
            return None
        return value