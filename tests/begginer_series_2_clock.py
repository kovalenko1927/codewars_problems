# https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python


def past(h, m, s):
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        return h * 3600000 + m * 60000 + s * 1000


def test_past():
    assert past(0, 1, 1) == 61000
