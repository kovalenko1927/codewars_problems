# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python


def accum(s):
    return "-".join([x.title() for x in [s[i] * (i + 1) for i in range(0, len(s))]])
    # return "-".join([x for x in [(s[i] * (i + 1)).title() for i in range(0, len(s))]])

# return '-'.join((a * i).title() for i, a in enumerate(s, 1))

print(accum('abc'))

def test_accum():
    assert accum("AqLx") == "A-Qq-Lll-Xxxx"


