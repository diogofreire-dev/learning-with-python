import pytest
from um import count

def test_standalone_um():
    """Test 'um' as a standalone word."""
    assert count("um") == 1
    assert count("hello, um, world") == 1
    assert count("um, thanks, um...") == 2

def test_case_insensitive():
    """Test case insensitivity."""
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("Um, thanks for the album. UM, it's great!") == 2

def test_with_punctuation():
    """Test 'um' with surrounding punctuation."""
    assert count("um?") == 1
    assert count("um!") == 1
    assert count("um.") == 1
    assert count("um,") == 1
    assert count("(um)") == 1

def test_within_words():
    """Test 'um' within words - should return 0."""
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrellas") == 0
    assert count("aluminum") == 0

def test_mixed_cases():
    """Test complex mixed scenarios."""
    assert count("um, album, Um, umbrella, UM") == 3
    assert count("yummy um aluminum UM umbrellas Um") == 3
    assert count("um...um...um") == 3
    assert count("um-um") == 2  # hyphen creates word boundary

def test_empty_and_spaces():
    """Test edge cases with empty strings and spaces."""
    assert count("") == 0
    assert count(" ") == 0
    assert count("   um   ") == 1