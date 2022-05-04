#!/usr/bin/python3

"""
Autre manière :
return set(set_1).intersection(set_2)
"""


def common_elements(set_1, set_2):
    return set(set_1) & set(set_2)
