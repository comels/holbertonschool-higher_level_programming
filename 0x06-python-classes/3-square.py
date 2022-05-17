#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A Square"""
    def __init__(self, size=0):
        """function that create a Square
        Args:
            size (int): size of the Square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        def area(self):
            """calculate the current square area

            Returns:
                int: the current square area
            """
            return self.__size ** 2
