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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self._Rectangle__height = value
        self._Rectangle__width = value

    def update(self, *args, **kwargs):
        """
        update the arguements in square objects
        """
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self._Rectangle__x = args[2]
            if len(args) > 3:
                self._Rectangle__y = args[3]
        else:
            if "id" in kwargs and kwargs["id"] is not None:
                self.id = kwargs["id"]
            if "size" in kwargs and kwargs["size"] is not None:
                self._Rectangle__height = kwargs["size"]
            if "size" in kwargs and kwargs["size"] is not None:
                self._Rectangle__width = kwargs["size"]
            if "x" in kwargs and kwargs["x"] is not None:
                self._Rectangle__x = kwargs["x"]
            if "y" in kwargs and kwargs["y"] is not None:
                self._Rectangle__y = kwargs["y"]

    def to_dictionary(self):
        """
        converts to dictionary
        """
        temp = {
            "id": self.id,
            "x": self._Rectangle__x,
            "size": self._Rectangle__height,
            "y": self._Rectangle__y,
        }
        return temp
