from plates import is_valid

def test_starting_with_letters():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False
    assert is_valid("A") == False

def test_length():
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_numbers_at_end():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AA22AA") == False

def test_first_number_not_zero():
    assert is_valid("AAA023") == False
    assert is_valid("AAA0") == False

def test_no_special_characters():
    assert is_valid("AAA.22") == False
    assert is_valid("AAA 22") == False
    assert is_valid("AAA-22") == False