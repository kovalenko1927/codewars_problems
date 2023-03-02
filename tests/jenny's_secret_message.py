# https://www.codewars.com/kata/55225023e1be1ec8bc000390/train/python
import pytest


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


@pytest.mark.parametrize("name, answer", [("Jin", "Hello, Jin!"),
                                         ("Johnny", "Hello, my love!")])
def test_greet(name, answer):
    assert greet(name) == answer

