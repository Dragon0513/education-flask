from service_layer.crypto.cryptorandom import CryptoRandom
import base64

def test_getRandom():
    """Test the getRandom method."""
    # Act
    result = CryptoRandom.get_random()
    result2 = CryptoRandom.get_random()
    # Assert
    assert result != result2

def test_getrandbits():
    """Test the getrandbits method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandbits(length)
    result2 = CryptoRandom.getrandbits(length)
    # Assert
    assert result != result2

def test_getrandbytes():
    """Test the getrandombytes method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandbytes(length)
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
    result2 = CryptoRandom.createuniqueidbase64(length)
    # Assert
    assert len(base64.b64decode(bytes(result, 'utf-8'))) == length
    assert result != result2

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.createuniqueidbase64(length)
    # Assert
    assert len(base64.b64decode(bytes(result, 'utf-8'))) == length

def test_getrandomstring():
    """Test the getrandomstring method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandomstring(length)
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

def test_getrandomstringbase64():
    """Test the getrandomstringbase64 method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandomstringbase64(length)
    result2 = CryptoRandom.getrandomstringbase64(length)
    # Assert

    #base64.b64decode(result)
    assert len(base64.b64decode(bytes(result, 'utf-8'))) == length
    assert result != result2

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.getrandomstringbase64(length)   
    # Assert
    assert len(base64.b64decode(bytes(result, 'utf-8'))) == length