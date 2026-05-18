from hello import hello

def test_default():
    assert hello("world") == "hello,world"

def test_important():
    assert hello("David") == "hello,David"    