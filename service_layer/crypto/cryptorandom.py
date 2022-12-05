import os
import random
import base64
from string import ascii_letters, digits
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
        return CryptoRandom._random.randint(0, 2**k - 1)

    @staticmethod
    def getrandbytes(k):
        """Return a string containing k random bytes."""
        return CryptoRandom.getrandbits(k * 8).to_bytes(k, 'big')
    @staticmethod
    def createuniqueid(length=32) -> str:
        """Return a unique id of a given length."""
        return CryptoRandom.getrandbytes(length).hex()[:length]

    @staticmethod
    def createuniqueidbase64(length=32) -> str:
        """Return a unique id of a given length."""
        return base64.b64encode(CryptoRandom.getrandbytes(length)).decode('utf-8')

    @staticmethod
    def getrandomstring(length=32) -> str:
        """Return a random string of a given length."""
        return ''.join(CryptoRandom._random.choice(ascii_letters+digits) for _ in range(length))
    
    @staticmethod
    def getrandomstringbase64(length=32) -> str:
        """Return a random string of a given length."""
        return base64.b64encode(CryptoRandom.getrandbytes(length)).decode('utf-8')