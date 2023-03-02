# https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python
import pytest


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


@pytest.mark.parametrize("distance, mpg, fuel, expected", [(50, 25, 2, True),
                                                           (100, 25, 3, False),
                                                           (12, 21, 4, True)])
def test_zero_fuel(distance, mpg, fuel, expected):
    assert zero_fuel(distance, mpg, fuel) == expected
