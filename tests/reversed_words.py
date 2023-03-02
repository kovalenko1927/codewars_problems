# https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python
import pytest


def reverse_words(s):
    return " ".join([i for i in s.split()][::-1])


@pytest.mark.parametrize("string, revers_str", [("hello word", "word hello"),
                                                ("this is lion king", "king lion is this")])
def test_reverse_words(string, revers_str):
    assert reverse_words(string) == revers_str


