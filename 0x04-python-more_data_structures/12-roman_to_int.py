#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string)==str:
        sum = 0
        for letter in roman_string:
            if letter == "I":
                sum += 1
                continue
            if letter == "V":
                sum += 5
                continue
            if letter == "X":
                sum += 10
                continue
            if letter == "L":
                sum += 50
                continue
            if letter == "C":
                sum += 100
                continue
            if letter == "D":
                sum += 500
                continue
            if letter == "M":
                sum += 1000
                continue
            else:
                return 0
        return sum
    else: 
        return 0
