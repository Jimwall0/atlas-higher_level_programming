#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    """
    A sqaure class with errors
    """
    def __init__(self, _Square__size=0):
        self._Square__size = _Square__size
        if not isinstance(_Square__size, int):
            raise TypeError("size must be an integer")
        if _Square__size < 0:
            raise ValueError("size must be >= 0")
