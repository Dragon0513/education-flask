from service_layer.crypto.cryptorandom import CryptoRandom
import time

def test_getRandom():

    result = CryptoRandom.get_random()
    time.sleep(.02)
    result2 = CryptoRandom.get_random()

    assert result == result2


        

def test_getrandbytes():
    """Test the getrandombytes method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandbytes(length)
    # Assert
    assert len(result) == length

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.getrandbytes(length)
    # Assert
    assert len(result) == length

def test_getrandomstring():
    """Test the getrandomstring method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandomstring(length)
    # Assert
    assert len(result) == length

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.getrandomstring(length)
    # Assert
    assert len(result) == length

def test_createuniqueid():
    """Test the createuniqueid method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.createuniqueid(length)
    # Assert
    assert len(result) == length

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.createuniqueid(length)
    # Assert
    assert len(result) == length