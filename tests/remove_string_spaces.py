"""
https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
"""
import pytest


def no_space(x):
    return x.replace(" ", "")


@pytest.mark.parametrize("string, expected", [("h e l l o", "hello"),
                                              (" king lion ", "kinglion"),
                                              ("   .    ", ".")])
def test_no_space(string, expected):
    assert no_space(string) == expected