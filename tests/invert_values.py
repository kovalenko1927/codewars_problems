# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
import pytest


def invert(lst):
    return [-i for i in lst]


@pytest.mark.parametrize("lst, expected", [([1, 2, 3], [-1, -2, -3]),
                                           ([-1, 9, -3], [1, -9, 3])])
def test_invert(lst, expected):
    assert invert(lst) == expected