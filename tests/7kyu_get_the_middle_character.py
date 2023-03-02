# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
import pytest


def get_middle(s):
    if len(s) % 2 != 0 :
        return s[len(s)//2]
    return s[(len(s)//2)-1:(len(s)//2)+1:]


@pytest.mark.parametrize("start_string, expected_string", [("A", "A"),
                                                           ("asvsa", "v"),
                                                           ("qqqbeqqq", "be")])
def test_get_middle(start_string, expected_string):
    assert get_middle(start_string) == expected_string

