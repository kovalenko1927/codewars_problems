# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python
import pytest


def find_smallest_int(arr):
    return min(arr)


@pytest.mark.parametrize("array, expected", [([1,3,5,3,4], 1),
                                             ([45,66,33], 33)])
def test_find_smallest_int(array, expected):
    assert find_smallest_int(array) == expected
