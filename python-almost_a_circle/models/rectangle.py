#!/usr/bin/python3
"""
file for square class
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a Rectangle class inheriting from the base class
    """
    def __init__(self, _Rectangle__width, _Rectangle__height,
                 _Rectangle__x=0, _Rectangle__y=0, id=None):
        super().__init__(id)
        if not isinstance(_Rectangle__width, int):
            raise TypeError("width must be an integer")
        elif _Rectangle__width <= 0:
            raise ValueError("width must be > 0")
        self._Rectangle__width = _Rectangle__width
        if not isinstance(_Rectangle__height, int):
            raise TypeError("height must be an integer")
        elif _Rectangle__height <= 0:
            raise ValueError("height must be > 0")
        self._Rectangle__height = _Rectangle__height
        if not isinstance(_Rectangle__x, int):
            raise TypeError("x must be an integer")
        elif _Rectangle__x < 0:
            raise ValueError("x must be >= 0")
        self._Rectangle__x = _Rectangle__x
        if not isinstance(_Rectangle__y, int):
            raise TypeError("y must be an integer")
        elif _Rectangle__y < 0:
            raise ValueError("y must be >= 0")
        self._Rectangle__y = _Rectangle__y

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self._Rectangle__width = value

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self._Rectangle__height = value

    @property
    def x(self):
        return self._Rectangle__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self._Rectangle__x = value

    @property
    def y(self):
        return self._Rectangle__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self._Rectangle__y = value

    def area(self,):
        """
        This is a method that returns area of
        rectangle
        """
        return self._Rectangle__height * self._Rectangle__width

    def display(self):
        """
        Prints a visual for the rectangle
        """
        for x in range(self._Rectangle__height):
            for y in range(self._Rectangle__width):
                print("#", end="")
            print("")