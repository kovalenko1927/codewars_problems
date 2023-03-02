# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
import pytest


def high_and_low(numbers):
    numbers = numbers.split()
    numbers = [int(i) for i in numbers]
    return str(max(numbers)) + " " + str(min(numbers))

print(high_and_low("1 -8 35 2"))


# return " ".join(max(list(numbers.split())) + min(list(numbers.split())))


@pytest.mark.parametrize("numbers, expected", [("2 3 6 7", "7 2"),
                                               ("0 6 -2 -6 1", "6 -6")])
def test_high_and_low(numbers, expected):
    assert high_and_low(numbers) == expected
