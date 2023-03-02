"""
https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python
"""
import pytest


def remove_char(s):
    return s[1:-1]


@pytest.mark.parametrize("string, expected", [("hello", "ell"),
                                              ("country", "ountr"),
                                              ("ball", "al")])
def test_remove_char(string, expected):
    assert remove_char(string) == expected
