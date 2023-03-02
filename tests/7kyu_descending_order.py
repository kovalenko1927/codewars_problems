# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python


def descending_order(num):
    return int("".join(map(str, sorted([i for i in str(num)], reverse=True))))


def test_descending_order():
    assert descending_order(1432) == 4321