#!/usr/bin/python3
"""
file for square class
"""
from base import Base


class Rectangle(Base):
    def __init__(self, _width, _height, _x=0, _y=0, id=None):
        super().__init__(id)
        self._width = _width
        self._height = _height
        self._x = _x
        self._y = _y
    
    @property
    def width(self):
        return self._width

    @_width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._height = value
