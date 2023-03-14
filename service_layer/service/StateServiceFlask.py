import datetime
import service_layer.crypto.JWTKeyManagement as jwt
from service_layer.service.StateService import StateService
from flask.sessions import SessionMixin
import service_layer.crypto.JWTKeyManagement as JWTKeyManagement

from service_layer.crypto.cryptorandom import CryptoRandom
class StateServiceFlask(StateService):
    ''' Stores data in the session. This is browser specific.'''
    session : SessionMixin
    def __init__(self, session):
        self.session = session
        
    def get_oidc_nonce(self):
        if 'nonce' in self.session:
            return self.session['nonce']
        else:
            nonce = CryptoRandom().getrandomstring(32)
            self.session['nonce'] = nonce
            return nonce

    # Consider using a state JWT as described in
    # https://tools.ietf.org/html/draft-bradley-oauth-jwt-encoded-state-09
    def get_oidc_state(self):
        if 'state' in self.session:
            return self.session['state']
        else:
            self.session['state'] = self.get_jwt_state()
            return self.session['state']


    def get_state_from_jwt(self, state_jwt):
        return JWTKeyManagement.load_jwt(state_jwt)