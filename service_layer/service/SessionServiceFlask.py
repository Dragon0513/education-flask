import datetime
import service_layer.crypto.JWTKeyManagement as JWTKeyManagement

from service_layer.crypto.cryptorandom import CryptoRandom


class Session(dict):
    """A dictionary that tracks modifications and expiration."""

    expiration = None
    modified = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.expiration = None
        self.modified = False

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.modified = True
        self.expiration = datetime.datetime.now() + datetime.timedelta(
            minutes=2
        )

    def __delitem__(self, key):
        super().__delitem__(key)
        self.modified = True

    def __getitem__(self, key):
        if self.is_expired():
            raise KeyError("Session expired")
        return super().__getitem__(key)

    def set_expiration(self, expiration):
        self.expiration = expiration

    def is_expired(self):
        if self.expiration is None:
            return False
        else:
            return datetime.datetime.now() > self.expiration


sessions: dict[str, Session] = {}  # key is nonce, value is session


# State JWT as described in
# https://tools.ietf.org/html/draft-bradley-oauth-jwt-encoded-state-09
def set_state_jwt(nonce_identifier: str, auth_login_url: str, tool_url: str):
    check_expiration()
    if nonce_identifier not in sessions:
        sessions[nonce_identifier] = Session()
    sessions[nonce_identifier]["state"] = CryptoRandom().getrandomstring(32)
    sessions[nonce_identifier][
        "state_jwt"
    ] = JWTKeyManagement.generate_state_jwt(
        nonce_identifier,
        sessions[nonce_identifier]["state"],
        auth_login_url,
        tool_url,
    )
    return sessions[nonce_identifier]["state_jwt"]


def set(nonce_identifier: str, key, value):
    if nonce_identifier not in sessions:
        sessions[nonce_identifier] = Session()
    sessions[nonce_identifier][key] = value


def get(nonce_identifier: str, key):
    check_expiration()
    if nonce_identifier in sessions:
        if key in sessions[nonce_identifier]:
            return sessions[nonce_identifier][key]
        else:
            return None
    else:
        return None


def check_expiration():
    """Remove expired sessions."""
    for nonce_identifier in list(sessions.keys()):
        if sessions[nonce_identifier].is_expired():
            del sessions[nonce_identifier]
