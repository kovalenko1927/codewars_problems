# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
import pytest


def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in sentence:
        if i in vowels:
            count +=1
    return count


@pytest.mark.parametrize("sentence, count", [("hello world", 3),
                                             ("xxx", 0),
                                             ("aa oo ee", 6)])
def test_get_count(sentence, count):
    assert get_count(sentence) == count