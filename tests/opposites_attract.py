# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python
import pytest


def lovefunc(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    return False


@pytest.mark.parametrize("flow_1, flow_2, result", [(1, 3, False),
                                                    (1, 2, True),
                                                    (2, 2, False),
                                                    (0, 1, True),
                                                    (0, 0, False)])
def test_love_func(flow_1, flow_2, result):
    assert lovefunc(flow_1, flow_2) == result