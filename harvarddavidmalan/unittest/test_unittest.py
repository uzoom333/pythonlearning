"""
#Dictionaries
#1-Normal use
def test_square():
    if square(2) != 4:
        print("2 squared is not 4")
    if square(3) != 9:
        print("3 squared is not 9")

#2-when use just the assert it have a AssertionError but now not have THE AssertionError , however not so good form because have so much lines of code
def square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")
    try:        
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared is not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared is not 0")        

"""
from unittest import square

def main():
    square()

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():    
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():    
    assert square(0) == 0

if __name__ == "__main__":
    main()