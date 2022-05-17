#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """_summary_
    """
    def __init__(self, size=0, position=(0, 0)):
        """Function that create a square

        Args:
            size (int): size of the square. Defaults to 0.
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Calculate the current square area

        Returns:
            int: the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """getting the size

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setting the size

        Args:
            value (int): the new size

        Raises:
            TypeError: exception
            ValueError: exception
        """
        self.__size = value

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """getting position

        Returns:
            tuple: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setting position

        Args:
            value (tuple): new position

        Raises:
            TypeError: tuple must be 2 positive int
        """
        self.__position = value

        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """function that prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        elif self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()

        for line in range(self.size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for colon in range(self.size):
                print("#", end="")
            print("")
