#!/usr/bin/python3

"""
def uniq_add(my_list=[]):
    sum = 0
    for number in set(my_list):
        sum += number
    return sum
"""


def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for number in my_list:
        if number not in new_list:
            new_list.append(number)
    for number in new_list:
        sum += number
    return sum
