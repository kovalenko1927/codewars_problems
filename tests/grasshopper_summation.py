# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
import pytest


def summation(num):
    return sum(i for i in range(1, num+1))


@pytest.mark.parametrize("number, expected", [(2, 3),
                                              (8, 36),
                                              (4, 10)])
def test_summation(number, expected):
    assert summation(number) == expected
