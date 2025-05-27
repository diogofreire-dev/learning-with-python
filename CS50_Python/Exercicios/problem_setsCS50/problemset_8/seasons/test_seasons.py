import pytest
from datetime import date
from seasons import convert_to_words

def test_convert_to_words():
    """Test number to words conversion"""
    assert convert_to_words(1) == "one"
    assert convert_to_words(60) == "sixty"
    assert convert_to_words(525600) == "five hundred twenty-five thousand, six hundred"
    assert convert_to_words(1051200) == "one million, fifty-one thousand, two hundred"

def test_convert_to_words_no_and():
    """Test that convert_to_words doesn't include 'and'"""
    result = convert_to_words(101)
    assert "and" not in result
    
    result = convert_to_words(1001)
    assert "and" not in result

def test_convert_to_words_zero():
    """Test zero conversion"""
    assert convert_to_words(0) == "zero"