# https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/python
import pytest


def maps(a):
    return [x * 2 for x in a]


@pytest.mark.parametrize("list, expected_lst", [([1, 2, 3], [2, 4, 6]),
                                                ([3, 4, 5], [6, 8, 10])])
def test_maps(list, expected_lst):
    assert maps(list) == expected_lst
