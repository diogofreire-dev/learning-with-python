import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    assert convert("1/1") == 100
    assert convert("0/1") == 0

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_convert_exceptions():
    # Test for ValueError - X greater than Y
    with pytest.raises(ValueError):
        convert("5/4")
    
    # Test for ValueError - Non-integers
    with pytest.raises(ValueError):
        convert("cat/dog")
    
    with pytest.raises(ValueError):
        convert("1.5/2")
    
    with pytest.raises(ValueError):
        convert("1/2.5")
    
    # Test for ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_edge_cases():
    # Test rounding behavior
    assert convert("1/3") == 33  # Should round to nearest int
    assert convert("2/3") == 67  # Should round to nearest int
    
    # Gauge edge cases
    assert gauge(1) == "E"
    assert gauge(99) == "F"