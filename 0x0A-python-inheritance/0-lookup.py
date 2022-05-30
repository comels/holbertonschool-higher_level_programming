#!/usr/bin/python3
"""the lookup function"""


def lookup(obj):
    """function that returns the list of
    available attributes and methods of an object

    Args:
        obj : object
    """
    return dir(obj)
