from bank import value

def test_hello_greeting():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0
    assert value("Hello, Newman") == 0

def test_h_greeting():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("Hi there") == 20
    assert value("How are you?") == 20
    assert value("H") == 20

def test_other_greeting():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("Yo") == 100
    assert value("1234") == 100
    assert value("") == 100