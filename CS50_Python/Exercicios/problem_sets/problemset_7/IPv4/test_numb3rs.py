from numb3rs import validate


def test_valid_ipv4_addresses():
    """Test various valid IPv4 addresses."""
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.1") == True
    assert validate("10.10.10.10") == True
    assert validate("172.16.0.1") == True


def test_invalid_ipv4_addresses():
    """Test various invalid IPv4 addresses."""
    # Octets greater than 255
    assert validate("275.3.6.28") == False
    assert validate("192.168.1.256") == False
    assert validate("300.300.300.300") == False
    
    # Incorrect number of octets
    assert validate("192.168.1") == False
    assert validate("1.2.3.4.5") == False
    
    # Non-numeric values
    assert validate("cat") == False
    assert validate("192.168.1.cat") == False
    assert validate("192.168.cat.1") == False
    
    # Incorrect format
    assert validate("192,168,1,1") == False
    assert validate("192 168 1 1") == False
    assert validate("...") == False
    
    # Empty string
    assert validate("") == False