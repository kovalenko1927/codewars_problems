"""
https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
"""
import pytest


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


@pytest.mark.parametrize("number, expected", [(2, "Even"),
                                              (4, "Even"),
                                              (3, "Odd"),
                                              (0, "Even"),
                                              (-24, "Even")])
def test_even_or_odd(number, expected):
    assert even_or_odd(number) == expected
