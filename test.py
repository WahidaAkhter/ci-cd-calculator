# pyrefly: ignore [missing-import]
import pytest
from calculator import add, subtract, multiply, divide, power


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5

    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(5, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -2) == 0.25

    with pytest.raises(ValueError, match="Zero cannot have a negative exponent"):
        power(0, -2)