from SessionService import SessionService
from flask.sessions import SessionMixin

from service_layer.crypto.cryptorandom import CryptoRandom
class SessionServiceFlask(SessionService):
    ''' Stores data in the session. This is browser specific.'''
    session : SessionMixin
    def __init__(self, session):
        self.session = session
        
    def get_oidc_nonce(self):
        if self.session.get('nonce'):
            return self.session.get('nonce')
        else:
            nonce = CryptoRandom().getrandomstring(32)
            self.session['nonce'] = nonce
            return nonce

    # Consider using a state JWT as described in
    # https://tools.ietf.org/html/draft-bradley-oauth-jwt-encoded-state-09
    def get_oidc_state(self):
        if self.session.get('state'):
            return self.session.get('state')
        else:
            state = CryptoRandom().getrandomstring(32)
            self.session['state'] = state
            return state