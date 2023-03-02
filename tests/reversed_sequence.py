# https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python
import pytest


def reverse_seq(n):
    lst = []
    for i in range(1, n+1):
        lst.append(i)
    lst.reverse()
    return lst

# return [x for x in range(n,0,-1)]


@pytest.mark.parametrize("number, expected_seq", [(3, [3, 2, 1]),
                                                  (5, [5, 4, 3, 2, 1])])
def test_revers_seq(number, expected_seq):
    assert reverse_seq(number) == expected_seq
