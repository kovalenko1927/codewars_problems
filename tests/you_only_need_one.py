# https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python
import pytest


def check(seq, elem):
    return elem in seq


@pytest.mark.parametrize("seq, elem, result", [([1, 2, 3], 2, True),
                                               ([2,3], 1, False)])
def test_check(seq, elem, result):
    assert check(seq, elem) == result