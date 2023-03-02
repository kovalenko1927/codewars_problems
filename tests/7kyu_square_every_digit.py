# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
import pytest


def square_digits(num):
    s = str([int(i) ** 2 for i in list(str(num))])
    x = s.translate({ord(i): None for i in ', []'})
    return int(x)


# ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)

@pytest.mark.parametrize("number, square", [(333, 999),
                                            (0, 0),
                                            (1256, 142536)])
def test_square(number, square):
    assert square_digits(number) == square


