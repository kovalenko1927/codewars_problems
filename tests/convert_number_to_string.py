"""
https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python
"""
import pytest


def number_to_string(num):
    return str(num)


@pytest.mark.parametrize("number, expected", [(123, "123"),
                                              (12345678, "12345678"),
                                              (-234, "-234"),
                                              (1+2, "3")])
def test_number_to_string(number, expected):
    assert number_to_string(number) == expected
