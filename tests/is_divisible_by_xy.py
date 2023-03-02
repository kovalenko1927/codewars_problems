# https://www.codewars.com/kata/5545f109004975ea66000086/train/python
import pytest


def is_divisible(n, x, y):
    return True if n % x == 0 and n % y == 0 else False


@pytest.mark.parametrize("n, x, y, expected", [(10, 5, 2, True),
                                               (4, 3, 1, False),
                                               (16, 3, 7, False),
                                               (18, 9, 2, True)])
def test_is_divisible(n, x, y, expected):
    assert is_divisible(n, x, y) == expected