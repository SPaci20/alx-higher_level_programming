#!/usr/bin/python3
"""Define a rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0  # Class attribute to keep track of instances

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the instance count

    @property
    def width(self):
        """Get a  method for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set a method for width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get a method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set a method for height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates and returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle with '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle using eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a deletion and decrements when a Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
