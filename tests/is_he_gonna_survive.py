# https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/python
import pytest


def hero(bullets, dragons):
    return True if bullets / dragons >= 2 else False


@pytest.mark.parametrize("bull, drag, res", [(10, 4, True),
                                             (5, 3, False)])
def test_hero(bull, drag, res):
    assert hero(bull, drag) == res

