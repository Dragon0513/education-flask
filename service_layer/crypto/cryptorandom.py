import random
import base64
class CryptoRandom(object):
    """A class that generates random numbers using the system's
    cryptographically secure random number generator.
    """
    _random = random.SystemRandom()

    def __init__(self):
        self._random = random.SystemRandom()

    @staticmethod
    def getrandbits(k):
        """Return a Python long containing k random bits."""
        return CryptoRandom._random.getrandbits(k)

    @staticmethod
    def getrandbytes(k):
        """Return a string containing k random bytes."""
        return CryptoRandom.getrandbits(k * 8).to_bytes(k, 'big')

    @staticmethod
    def createuniqueid(length=32) -> str:
        """Return a unique id of a given length."""
        return CryptoRandom.getrandbytes(length).hex()

    @staticmethod
    def createuniqueidbase64(length=32) -> str:
        """Return a unique id of a given length."""
        return base64.b64encode(CryptoRandom.getrandbytes(length)).decode('utf-8')

    @staticmethod
    def getrandomstring(length=32) -> str:
        """Return a random string of a given length."""
        return CryptoRandom.getrandbytes(length).decode('utf-8')
    
    @staticmethod
    def getrandomstringbase64(length=32) -> str:
        """Return a random string of a given length."""
        return base64.b64encode(CryptoRandom.getrandbytes(length)).decode('utf-8')