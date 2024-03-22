#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_no = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    result = 0
    value = 0
    prev = 0
    for i in reversed(roman_string):
        value = roman_no[i]
        if value > prev:
            result += value
        else:
            result -= value
        prev = value

    return result
