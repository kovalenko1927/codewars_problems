# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python
import pytest


def abbrev_name(name):
    lst = []
    for i in name.split():
        lst.append(i[0].upper())
    return f"{lst[0]}.{lst[1]}"

# first, last = name.upper().split(' ')
#     return first[0] + '.' + last[0]


@pytest.mark.parametrize("name, abbrev", [("Vova Kovalenko", "V.K"),
                                          ("Vadym B", "V.B"),
                                          ('S Karina', "S.K")])
def test_abbrev_name(name, abbrev):
    assert abbrev_name(name) == abbrev
