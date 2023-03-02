# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
import pytest


def find_needle(haystack):
    for i in haystack:
        if i == "needle":
            return f"found the needle at position {haystack.index(i)}"

# return f"found the needle at position {haystack.index('needle')}"


@pytest.mark.parametrize("haystack, expected", [([1, 'needle'], "found the needle at position 1"),
                                                (['qw', 1, 'er', 'needle'], "found the needle at position 3")])
def test_find_needle(haystack, expected):
    assert find_needle(haystack) == expected
