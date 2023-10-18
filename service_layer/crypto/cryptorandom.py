import base64
import random
import time
from string import ascii_letters, digits


class CryptoRandom(object):
    """A class that generates random numbers using the system's
    cryptographically secure random number generator.
    """

    @staticmethod
    def get_random():
        return random.SystemRandom(time.time())

    @staticmethod
    def getrandbits(k):
        """Return a Python long containing k random bits."""
        return CryptoRandom.get_random().randint(0, 2**k - 1)

    @staticmethod
    def getrandbytes(k):
        """Return a string containing k random bytes."""
        return CryptoRandom.getrandbits(k * 8).to_bytes(k, "big")

    @staticmethod
    def createuniqueid(length=32) -> str:
        """Return a unique id of a given length."""
        return CryptoRandom.getrandbytes(length).hex()[:length]

    @staticmethod
    def createuniqueidbase64(length=32) -> str:
        """Return a unique id of a given length."""
        return base64.b64encode(CryptoRandom.getrandbytes(length)).decode("utf-8")

    @staticmethod
    def getrandomstring(length=32) -> str:
        """Return a random string of a given length."""
        return "".join(
            CryptoRandom.get_random().choice(ascii_letters + digits)
            for _ in range(length)
        )

    @staticmethod
    def getrandomstringbase64(length=32) -> str:
        """Return a random string of a given length."""
        return base64.b64encode(CryptoRandom.getrandbytes(length)).decode("utf-8")
