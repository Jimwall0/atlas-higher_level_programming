#!/usr/bin/python3
"""
file for square class
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a Rectangle class inheriting from the base class
    """
    def __init__(self, _Rectangle__width, _Rectangle__height,
                 _Rectangle__x=0, _Rectangle__y=0, id=None):
        super().__init__(id)
        if not isinstance(_Rectangle__width, int):
            raise TypeError("width must be an integer")
        elif _Rectangle__width <= 0:
            raise ValueError("width must be > 0")
        self._Rectangle__width = _Rectangle__width
        if not isinstance(_Rectangle__height, int):
            raise TypeError("height must be an integer")
        elif _Rectangle__height <= 0:
            raise ValueError("height must be > 0")
        self._Rectangle__height = _Rectangle__height
        if not isinstance(_Rectangle__x, int):
            raise TypeError("x must be an integer")
        elif _Rectangle__x < 0:
            raise ValueError("x must be >= 0")
        self._Rectangle__x = _Rectangle__x
        if not isinstance(_Rectangle__y, int):
            raise TypeError("y must be an integer")
        elif _Rectangle__y < 0:
            raise ValueError("y must be >= 0")
        self._Rectangle__y = _Rectangle__y

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self._Rectangle__width = value

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self._Rectangle__height = value

    @property
    def x(self):
        return self._Rectangle__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self._Rectangle__x = value

    @property
    def y(self):
        return self._Rectangle__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self._Rectangle__y = value

    def area(self,):
        """
        This is a method that returns area of
        rectangle
        """
        return self._Rectangle__height * self._Rectangle__width

    def display(self):
        """
        Prints a visual for the rectangle
        """
        for y in range(self._Rectangle__height):
            if y == 0:
                for _ in range(self.y):
                    print("")
            for x in range(self._Rectangle__width):
                if x == 0:
                    for _ in range(self.x):
                        print(" ", end="")
                print("#", end="")
            print("")

    def __str__(self):
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y}"
            f" - {self._Rectangle__width}/{self._Rectangle__height}"
        )

    def update(self, *args, **kwargs):
        """
        updates the values inside arguements
        """
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self._Rectangle__width = args[1]
            if len(args) > 2:
                self._Rectangle__height = args[2]
            if len(args) > 3:
                self._Rectangle__x = args[3]
            if len(args) > 4:
                self._Rectangle__y = args[4]
        else:
            if "id" in kwargs and kwargs["id"] is not None:
                self.id = kwargs["id"]
            if "width" in kwargs and kwargs["width"] is not None:
                self._Rectangle__width = kwargs["width"]
            if "height" in kwargs and kwargs["height"] is not None:
                self._Rectangle__height = kwargs["height"]
            if "x" in kwargs and kwargs["x"] is not None:
                self._Rectangle__x = kwargs["x"]
            if "y" in kwargs and kwargs["y"] is not None:
                self._Rectangle__y = kwargs["y"]
