import pytest
from Calculator import add, sub, multiply, divide


def test_raises_exception_on_string_arguments():
    with pytest.raises(TypeError):
        add('jeden')


def test_add():
    assert add([8, 2, 5]) == 15


def test_subtract():
    assert sub(7, 5) == 2


def test_multiply():
    assert multiply([2, 2, 5]) == 20


def test_divide():
    assert divide(10, 5) == 2
