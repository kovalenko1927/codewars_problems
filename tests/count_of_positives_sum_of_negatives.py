# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
from typing import List, Any

import pytest


def count_positives_sum_negatives(arr):
    pos_lst = []
    neg_lst = []
    final_lst = []
    if len(arr) == 0:
        return final_lst
    for i in arr:
        if i > 0:
            pos_lst.append(i)
        elif i < 0:
            neg_lst.append(i)
    final_lst.append(len(pos_lst))
    final_lst.append(sum(neg_lst))
    return final_lst

# return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []


@pytest.mark.parametrize("start_arr, final_arr", [([1, 2, 3, -5, -7], [3, -12]),
                                                  ([4, -1, 5, -6, 4, -9], [3, -16]),
                                                  ([], [])])
def test_count_pos_neg(start_arr, final_arr):
    assert count_positives_sum_negatives(start_arr) == final_arr

