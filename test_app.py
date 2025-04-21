import pytest
from app import (
    add,
    subtract,
    multiply,
    divide,
    square_root,
    is_even,
    to_upper
)


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_square_root():
    assert square_root(9) == 3.0


def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-4)


def test_is_even_true():
    assert is_even(4) is True


def test_is_even_false():
    assert is_even(5) is False


def test_to_upper():
    assert to_upper("hello") == "HELLO"


def test_to_upper_non_string():
    with pytest.raises(TypeError):
        to_upper(123)
