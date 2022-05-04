#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    sum = 0
    for letter in roman_string:
        if letter == "I":
            sum += 1
        elif letter == "V":
            sum += 5
        elif letter == "X":
            sum += 10
        elif letter == "L":
            sum += 50
        elif letter == "C":
            sum += 100
        elif letter == "D":
            sum += 500
        elif letter == "M":
            sum += 1000
        else:
            return 0
    return sum
