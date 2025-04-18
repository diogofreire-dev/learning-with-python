from twttr import shorten

def test_lowercase_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("aeiou") == ""

def test_uppercase_vowels():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"
    assert shorten("AEIOU") == ""

def test_mixed_case():
    assert shorten("Twitter") == "Twttr"
    assert shorten("HeLlO") == "HLl"
    assert shorten("AeIoU") == ""

def test_no_vowels():
    assert shorten("rhythm") == "rhythm"
    assert shorten("RHYTHM") == "RHYTHM"
    assert shorten("psych") == "psych"

def test_numbers_and_symbols():
    assert shorten("h3ll0") == "h3ll0"
    assert shorten("c@ts!") == "c@ts!"
    assert shorten("123") == "123"

def test_empty_string():
    assert shorten("") == ""

def test_mixed_content():
    assert shorten("CS50 is awesome!") == "CS50 s wsm!"
    assert shorten("Programming 101") == "Prgrmmng 101"