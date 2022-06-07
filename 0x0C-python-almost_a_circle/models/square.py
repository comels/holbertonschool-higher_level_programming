#!/usr/bin/python3
"""the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Function that define the __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """function that return the size"""
        return self.width

    @size.setter
    def size(self, value):
        """function that set the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """function that assigns an argument to each attribute"""
        attr = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i != 4:
                    setattr(self, attr[i], arg)
        else:
            for key in kwargs:
                if key in attr:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
