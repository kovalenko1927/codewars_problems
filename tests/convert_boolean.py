"""
https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python
"""
import pytest


def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"


@pytest.mark.parametrize("boolean, expected", [(True, "Yes"),
                                               (False, "No")])
def test_bool_to_word(boolean, expected):
    assert bool_to_word(boolean) == expected