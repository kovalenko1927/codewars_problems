# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
import pytest


def digitize(n):
    lst = []
    for i in str(n)[::-1]:
        lst.append(int(i))
    return lst

# return map(int, str(n)[::-1])


@pytest.mark.parametrize("number, expected_list", [(123, [3, 2, 1]),
                                                   (54321, [1, 2, 3, 4, 5])])
def test_digitize(number, expected_list):
    assert digitize(number) == expected_list
