"""
https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
"""
import pytest


def make_negative(number):
    return -abs(number)


@pytest.mark.parametrize("number, expected", [(-5, -5),
                                              (0, 0),
                                              (33, -33)])
def test_make_negative(number, expected):
    assert make_negative(number) == expected