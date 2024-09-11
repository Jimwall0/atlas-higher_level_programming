#!/usr/bin/python3
"""
This is code for a rectangle class
"""


class Rectangle:
    """
    This is the class for rectangle
    """
    def __init__(self, _Rectangle__width=0, _Rectangle__height=0):
        if not isinstance(_Rectangle__width, int):
            raise TypeError("width must be an integer")
        elif _Rectangle__width < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = _Rectangle__width
        if not isinstance(_Rectangle__height, int):
            raise TypeError("height must be an integer")
        elif _Rectangle__height < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = _Rectangle__height

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def area(self):
        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return 0
        return 2*(self._Rectangle__height + self._Rectangle__width)

    def __str__(self):
        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return ""
        string = ""
        for colomn in range(self._Rectangle__height):
            for row in range(self._Rectangle__width):
                string += "#"
            if not colomn == self._Rectangle__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return f"Rectangle({self._Rectangle__width}, "\
            f"{self._Rectangle__height})"
