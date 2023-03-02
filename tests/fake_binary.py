# https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python
import pytest


def fake_bin(x):
    lst = []
    for i in x:
        if int(i) >= 5:
            lst.append('1')
        elif int(i) < 5:
            lst.append('0')
    return ''.join(lst)
# return ''.join('0' if int(c) < 5 else '1' for c in s)


@pytest.mark.parametrize("string, expected", [('12345678', '00001111'),
                                              ('1278', '0011'),
                                              ('9871', '1110')])
def test_fake_bin(string, expected):
    assert fake_bin(string) == expected