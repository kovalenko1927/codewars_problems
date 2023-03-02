# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python
import pytest


def century(year):
    if year % 100 > 0:
        return year // 100 + 1
    return year // 100


@pytest.mark.parametrize("year, expected_century", [(1300, 13),
                                                    (1265, 13),
                                                    (2001, 21),
                                                    (1900, 19)])
def test_century(year, expected_century):
    assert century(year) == expected_century