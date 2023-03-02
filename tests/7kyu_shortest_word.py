# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

def find_short(s):
    return len(min(s.split(), key=len))


def test_find_short():
    assert find_short("ball letter football spring war") == 3