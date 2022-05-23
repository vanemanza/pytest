
import pytest


def func(x):
    return x + 2

#@pytest.mark.este_si
def test_answer():
    assert func(3) == 5
