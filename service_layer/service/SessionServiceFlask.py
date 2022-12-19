import datetime
import jwt
from service_layer.service.SessionService import SessionService
from flask.sessions import SessionMixin
import service_layer.crypto.CryptoKeyManagement as CryptoKeyManagement

from service_layer.crypto.cryptorandom import CryptoRandom
class SessionServiceFlask(SessionService):
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
    
    def get_jwt_state(self):
        state = CryptoRandom().getrandomstring(32)
        return state
        state_jwt = {
            'state': state,
            'nonce': self.get_oidc_nonce(),
            'iat': datetime.datetime.utcnow().timestamp(),
            'exp': (datetime.datetime.utcnow() + datetime.timedelta(minutes=60)).timestamp(),
            'kid': 'backendprivatekey',
            'iss': 'https://localhost:5000'
        }
        return CryptoKeyManagement.sign_jwt(state_jwt)


    def get_state_from_jwt(self, state_jwt):
        return CryptoKeyManagement.load_jwt(state_jwt)