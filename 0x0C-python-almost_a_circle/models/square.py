#!/usr/bin/python3
"""the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """Function that define the __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """function that return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """function that set the size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """function that assigns an argument to each attribute"""
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "x" in kwargs:
                self.x = kwargs["x"]

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }