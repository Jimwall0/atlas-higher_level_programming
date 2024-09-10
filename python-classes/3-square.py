#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 2-square.py)
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
