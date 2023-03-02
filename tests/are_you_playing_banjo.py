# https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python
import pytest


def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0:1].lower() == "r" else f"{name} does not play banjo"


@pytest.mark.parametrize("name, expected", [("martin", "martin does not play banjo"),
                                            ("Rikke", "Rikke plays banjo")])
def test_are_you_play(name, expected):
    assert are_you_playing_banjo(name) == expected