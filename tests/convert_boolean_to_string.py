# https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
import pytest


def boolean_to_string(b):
    return "True" if b else "False"


@pytest.mark.parametrize("first, last", [(1, "True"),
                                           (0, "False")])
def test_bool_to_string(first, last):
    assert boolean_to_string(first) == last
