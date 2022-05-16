#!/usr/bin/python3
from decimal import DivisionByZero
import re


def safe_print_division(a, b):
    try:
        result = a / b
    except DivisionByZero:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
