#!/usr/bin/python3
"""Define a class BaseGeometry."""


class BaseGeometry:
    """Represent BaseGeometry."""
    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""Define a class Rectangle, inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
    """Instation of width and height."""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
