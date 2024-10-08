#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 5-square.py)
"""


class Square:
    """
    This is the square class
    """
    def __init__(self, _Square__size=0, _Square__position=(0, 0)):
        self._Square__size = _Square__size
        if not isinstance(_Square__size, int):
            raise TypeError("size must be an integer")
        if _Square__size < 0:
            raise ValueError("size must be >= 0")
        if isinstance(_Square__position, tuple):
            TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(_Square__position[0], int):
            TypeError("position must be a tuple of 2 positive integers")
        if _Square__position[0] < 0:
            TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(_Square__position[1], int):
            TypeError("position must be a tuple of 2 positive integers")
        if _Square__position[1] < 0:
            TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = _Square__position

    def area(self):
        return self._Square__size * self._Square__size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        self._Square__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        for loop in range(self._Square__size):
            for num in range(self._Square__size):
                print("#", end="")
            print()
        if self._Square__size == 0:
            print()

    @property
    def position(self):
        return self._Square__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0:
            TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0:
            TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value
