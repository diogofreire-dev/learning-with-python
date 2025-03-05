from hello import hello

def test_argument():
    assert hello("David") == "hello, David"

def test_argument2():
    for name in ["John", "Mary", "Peter" ]:
        assert hello(name) == f"hello, {name}"

def test_default():
    assert hello() == "hello, world"
