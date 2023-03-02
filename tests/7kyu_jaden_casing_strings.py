# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
import re


def to_jaden_case(string):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo:
                  mo.group(0)[0].upper() +
                  mo.group(0)[1:].lower(), string)

# import string
# toJadenCase = string.capwords

# return ' '.join(word.capitalize() for word in string.split())

def test_to_jaden_case():
    assert to_jaden_case("How can mirrors be real if our eyes aren't real") == "How Can Mirrors Be Real If Our Eyes Aren't Real"