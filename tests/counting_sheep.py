# https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
import pytest


def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s:
            count += 1
    return count


@pytest.mark.parametrize("sheep, number", [([True, True, True, False,
                                             True, True, True, True,
                                             True, False, True, False,
                                             True, False, False, True,
                                             True, True, True, True,
                                             False, False, True, True], 17),
                                           ([True, True, True, False,
                                             True, True, True, True,
                                             True, False, True, False,
                                             True, False, False, True,
                                             True, True, True, True,
                                             False, False], 15)])
def test_count_sheeps(sheep, number):
    assert count_sheeps(sheep) == number

