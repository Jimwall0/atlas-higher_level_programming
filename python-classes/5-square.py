#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 4-square.py)
"""


class Square:
    """
    This is the square class
    """
    def __init__(self, _Square__size=0):
        self._Square__size = _Square__size
        if not isinstance(_Square__size, int):
            raise TypeError("size must be an integer")
        if _Square__size < 0:
            raise ValueError("size must be >= 0")

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
