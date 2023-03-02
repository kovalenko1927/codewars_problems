"""
https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python
"""
import pytest


def repeat_str(repeat, string):
    return repeat * string


@pytest.mark.parametrize("number, string, expected", [(2, "hello", "hellohello"),
                                                      (5, "a", "aaaaa"),
                                                      (3, "abc", "abcabcabc")])
def test_repeat_str(number, string, expected):
    assert repeat_str(number, string) == expected