# https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python
import pytest


def greet(name):
    return f"Hello, {name} how are you doing today?"


@pytest.mark.parametrize("name, expected_res", [("Vova", "Hello, Vova how are you doing today?"),
                                                ("Vika", "Hello, Vika how are you doing today?")])
def test_greet(name, expected_res):
    assert greet(name) == expected_res