# https://www.codewars.com/kata/582cb0224e56e068d800003c/train/python
import pytest


def litres(time):
    return int(time * 0.5)


@pytest.mark.parametrize("time, liters", [(3, 1),
                                          (6, 3),
                                          (12.3, 6),
                                          (1.4, 0)])
def test_litres(time, liters):
    assert litres(time) == liters