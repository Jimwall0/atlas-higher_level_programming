#!/usr/bin/python3
"""
File for square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is a square class that copies from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        )

    @property
    def size(self):
        return self._Rectangle__height

    @size.setter
    def size(self, value):
        self._Rectangle__height = value
        self._Rectangle__width = value
