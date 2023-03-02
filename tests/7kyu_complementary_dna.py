# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python


def DNA_strand(dna):
    var = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([var[x] for x in dna])


def test_DNA():
    assert DNA_strand("ATCG") == "TAGC"





