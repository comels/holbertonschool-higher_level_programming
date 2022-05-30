#!/usr/bin/python3
"""the is_same_class function"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.

    To know if the precise type of obj is a_class
    (and not a subtype of a_class), use the type function.
    """
    return type(obj) is a_class
