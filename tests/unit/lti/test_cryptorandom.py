from service_layer.crypto.cryptorandom import CryptoRandom
import time

def test_getRandom():
    """Test the getRandom method."""
    # Act
    result = CryptoRandom.get_random()
    time.sleep(.02)
    result2 = CryptoRandom.get_random()
    # Assert
    assert result != result2

def test_getrandbits():
    """Test the getrandbits method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandbits(length)
    time.sleep(.02)
    result2 = CryptoRandom.getrandbits(length)
    # Assert
    assert result == result2

def test_getrandbytes():
    """Test the getrandombytes method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandbytes(length)
    time.sleep(.02)
    result2 = CryptoRandom.getrandbytes(length)
    # Assert
    assert len(result) == length
    assert result != result2

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.getrandbytes(length)
    # Assert
    assert len(result) == length

def test_createuniqueid():
    """Test the createuniqueid method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.createuniqueid(length)
    time.sleep(.02)
    result2 = CryptoRandom.createuniqueid(length)
    # Assert
    assert len(result) == length
    assert result != result2

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.createuniqueid(length)
    # Assert
    assert len(result) == length

def test_createuniqueidbase64():
    """Test the createuniqueidbase64"""

    # Arrange
    length = 32
    # Act
    result = CryptoRandom.createuniqueidbase64(length)
    time.sleep(.02)
    result2 = CryptoRandom.createuniqueidbase64(length)
    # Assert
    assert len(result) == length
    assert result != result2

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.createuniqueidbase64(length)
    # Assert
    assert len(result) == length

def test_getrandomstring():
    """Test the getrandomstring method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandomstring(length)
    time.sleep(.02)
    result2 = CryptoRandom.getrandomstring(length)
    # Assert
    assert len(result) == length
    assert result != result2

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.getrandomstring(length)
    # Assert
    assert len(result) == length