class SessionService(object):
    def __init__(self, request):
        self._request = request

    def get_nonce(self):
        return 'nonce'

    def get_state(self):
        return 'state'