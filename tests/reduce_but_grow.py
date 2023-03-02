# https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python


def grow(arr):
    answer = 1
    for i in arr:
        answer *= i
    return answer


def test_grow():
    assert grow([3, 5, 6]) == 90