# https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python


def bmi(weight, height):
    bm_index = weight / height ** 2
    if bm_index <= 18.5:
        return "Underweight"
    elif bm_index <= 25:
        return "Normal"
    elif bm_index <= 30:
        return "Overweight"
    else:
        return "Obese"


def test_bmi():
    assert bmi(66, 1.79) == "Normal"
