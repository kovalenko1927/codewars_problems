# https://www.codewars.com/kata/5601409514fc93442500010b/train/python
import pytest


def better_than_average(class_points, your_points):
    return True if sum(class_points) / len(class_points) < your_points else False


@pytest.mark.parametrize("class_p, your, expected", [([1, 4, 5], 7, True),
                                                   ([5, 6, 8], 2, False)])
def test_better_than_avewrage(class_p, your, expected):
    assert better_than_average(class_p, your) == expected