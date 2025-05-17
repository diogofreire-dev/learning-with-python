import pytest
from working import convert

def test_standard_format():
    """Test standard format with full time specifications."""
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 6:45 PM") == "10:30 to 18:45"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"

def test_omitted_minutes():
    """Test formats with omitted minutes."""
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

def test_overnight_hours():
    """Test scenarios with overnight hours."""
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("11:30 PM to 7:15 AM") == "23:30 to 07:15"

def test_invalid_format():
    """Test invalid formats that should raise ValueError."""
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")  # Wrong separator
    
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")  # Missing AM/PM
    
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")  # Missing space before AM/PM

def test_invalid_times():
    """Test invalid time values that should raise ValueError."""
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")  # Hour > 12
    
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")  # Minute > 59
    
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")  # Hour > 12
    
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")  # Minute > 59