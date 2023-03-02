# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python


def disemvowel(string_):
    return string_.translate({ord(i): None for i in 'aeuioAEUIO'})

# return string.translate(None, 'aeiouAEIOU')

# return "".join(c for c in string if c.lower() not in "aeiou")

# for i in "aeiouAEIOU":
#   s = s.replace(i,'')
# return s


def test_disemvowel():
    assert disemvowel("HELLO, you ARe FaKE!") == 'HLL, y R FK!'
