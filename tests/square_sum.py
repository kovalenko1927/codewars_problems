# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
import pytest


def square_sum(numbers):
    # return sum(x ** 2 for x in numbers) - best solution
    lst = []
    for i in numbers:
        x = i ** 2
        lst.append(x)
    return sum(lst)


@pytest.mark.parametrize("numbers, expected", [([1, 2, 2], 9),
                                               ([-1, -2], 5),
                                               ([], 0)])
def test_square_sum(numbers, expected):
    assert square_sum(numbers) == expected