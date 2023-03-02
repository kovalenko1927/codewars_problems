# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python
import pytest


def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


@pytest.mark.parametrize("num, expected", [([1, 2, 3], 2),
                                           ([], 0),
                                           ([-2, 6, 8], 4)])
def test_find_average(num, expected):
    assert find_average(num) == expected
