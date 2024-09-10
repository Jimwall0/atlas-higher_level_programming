#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    def __init__(self, _Square__size = 0):
        self._Square__size = _Square__size
        if type(_Square__size) != int:
            raise TypeError("size must be an integer")
        if _Square__size < 0:
            raise ValueError("size must be >= 0")