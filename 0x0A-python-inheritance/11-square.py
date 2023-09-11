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


"""Define a class Rectangle, inherited from BaseGeometry."""


class Rectangle(BaseGeometry):
    """Represents a rectangle class."""
    def __init__(self, width, height):
        """Instatiation of width and height."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Return area."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str()."""
        return f"[Rectangle] {self.__width}/{self.__height}"


"""Define a class Square, inherited from Rectangle."""


class Square(Rectangle):
    """Represent Square class."""
    def __init__(self, size):
        """Initialize size."""
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def __str__(self):
        """Return the print() and str()."""
        return f"[Square] {self.__size}/{self.__size}"
