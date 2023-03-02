"""
https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
"""
import pytest


def solution(string):
    return string[::-1]


@pytest.mark.parametrize("string, expected", [("world", "dlrow"),
                                              ("hello", "olleh"),
                                              ('', ''),
                                              ("h", "h")])
def test_solution(string, expected):
    assert solution(string) == expected
