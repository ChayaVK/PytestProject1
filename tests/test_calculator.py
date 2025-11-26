import pytest

from Apps.Calculator import add, subtract, multiply, divide

def test_add():
    assert add(1,2) == 3
    assert add(-1,-2) == -3
    assert add(-5,+10) == 5
    assert add(6,-12)==-6


def test_sub():
    assert subtract(1,2) == -1
    assert subtract(-1,2) == -3

def test_multiply():
    assert multiply(1,2) == 2
    assert multiply(-1,2) == -2

def test_divide():
    assert divide(2,2) == 1
    assert divide(10,5) == 2
    divide(10,0)

