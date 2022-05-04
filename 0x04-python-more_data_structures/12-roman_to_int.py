#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) == 0 or roman_string is None:
        return 0
    sum = 0
    for letter in roman_string:
        if letter not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
            return 0
        if letter == "I":
            sum += 1
        if letter == "V":
            sum += 5
        if letter == "X":
            sum += 10
        if letter == "L":
            sum += 50
        if letter == "C":
            sum += 100
        if letter == "D":
            sum += 500
        if letter == "M":
            sum += 1000
    return sum
