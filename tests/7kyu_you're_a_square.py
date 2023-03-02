# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
import pytest


def is_square(n):
    return True if (pow(n, .5)) ** 2 == n else False

# return True if int(pow(n, .5)) * int(pow(n, .5)) == n else False
# return True if n*n//n == n else False


@pytest.mark.parametrize("get_int, expected", [(4, True),
                                               (0, True),
                                               (-1, False),
                                               (3, False)])
def test_is_square(get_int, expected):
    assert is_square(get_int) == expected
