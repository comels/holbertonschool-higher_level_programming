#!/usr/bin/python3
"""the BaseGeometry class"""


class BaseGeometry():
    """the BaseGeometry class"""
    def area(self):  # sourcery skip: raise-specific-error
        """function that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
