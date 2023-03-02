# https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python
import pytest


def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0


@pytest.mark.parametrize("n, m, res", [(1, 5, 5),
                                       (0, 5, 0),
                                       (-1, 0, 0)])
def test_paperwork(n, m, res):
    assert paperwork(n, m) == res

