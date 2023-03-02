# https://www.codewars.com/kata/544675c6f971f7399a000e79/train/python
import pytest


def string_to_number(s):
    return int(s)


@pytest.mark.parametrize("string, num", [('123', 123),
                                      ('3454', 3454),
                                      ('0', 0)])
def test_str_to_num(string, num):
    assert string_to_number(string) == num