# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
import pytest


def is_isogram(string):
    count = 0
    for i in range(len(string)):
        if string[i].lower() in string[i + 1:].lower():
            count += 1
    if count > 0:
        return False
    return True

# return len(string) == len(set(string.lower()))

@pytest.mark.parametrize("start_word, expected_result", [("word", True),
                                                         ("Hello", False),
                                                         ("", True),
                                                         ("isIgnore", False)])
def test_is_isogram(start_word, expected_result):
    assert is_isogram(start_word) == expected_result
