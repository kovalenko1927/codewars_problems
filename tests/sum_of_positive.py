"""
https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
"""
import pytest


def positive_sum(arr):
    positive_lst = []
    for i in arr:
        if i >= 0:
            positive_lst.append(i)
    if len(positive_lst) > 0:
        return sum(positive_lst)
    return 0


@pytest.mark.parametrize("arr, expected", [([1, 2, 3], 6),
                                           ([1, -5, 2], 3),
                                           ([-3, -3], 0),
                                           ([], 0)])
def test_positive_sum(arr, expected):
    assert positive_sum(arr) == expected
