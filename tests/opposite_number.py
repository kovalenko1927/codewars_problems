"""
https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python
"""
import pytest


def opposite(number):
    if number > 0:
        return -abs(number)
    return abs(number)


@pytest.mark.parametrize("number, expected", [(1, -1),
                                              (-2, 2),
                                              (0, 0),
                                              (3.45, -3.45),
                                              (9.99, -9.99)])
def test_opposite(number, expected):
    assert opposite(number) == expected
