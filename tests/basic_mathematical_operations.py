# https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
import pytest


def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    else:
        if operator == '/' and value2 != 0:
            return value1 / value2


# return eval(f'{value1}{operator}{value2}')


@pytest.mark.parametrize("operator, num1, num2, result", [('+', 4, 2, 6),
                                                          ('-', 6, 2, 4),
                                                          ('*', 2, 2, 4),
                                                          ('/', 8, 2, 4)])
def test_basic_op(operator, num1, num2, result):
    assert basic_op(operator, num1, num2) == result
