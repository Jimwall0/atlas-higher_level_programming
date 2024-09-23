#!/usr/bin/python3
"""
file for square class
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a Rectangle class inheriting from the base class
    """
    def __init__(self, _Rectangle__width, _Rectangle__height, _Rectangle__x=0, _Rectangle__y=0, id=None):
        super().__init__(id)
        self._Rectangle__width = _Rectangle__width
        self._Rectangle__height = _Rectangle__height
        self._Rectangle__x =_Rectangle__x
        self._Rectangle__y = _Rectangle__y

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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__height = value

    @property
    def x(self):
        return self._Rectangle__x

    @x.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__x = value

    @property
    def y(self):
        return self._Rectangle__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__y = value
