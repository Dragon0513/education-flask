from service_layer.lti import LaunchDataStorage
import time

#pytest tests\unit\lti\test_LaunchDataStorage.py --cov

def test_get_set_value():
    """Test if a assigned value for a specific key is correctly stored."""
    # Arrange
    key = "testkeystring"
    value = 25

    # Act
    LaunchDataStorage.set_value(key, value)

    # Assert
    assert LaunchDataStorage.get_value(key) == value

def test_expiration():
    """Test if a key can be access after the expiration time."""
    # Arrange
    key = "othertestkeystring"
    value = 25

    # Act
    LaunchDataStorage.set_value(key, value)
    time.sleep(62)

    # Assert
    assert LaunchDataStorage.get_value(key) == None



