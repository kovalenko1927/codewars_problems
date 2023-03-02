# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python


def filter_list(l):
    return [i for i in l if type(i) == type(1)]

#return [i for i in l if not isinstance(i, str)]


def test_filter_list():
    assert filter_list([1, 'q', 45, '123', 5, '', 4]) == [1, 45, 5, 4]
