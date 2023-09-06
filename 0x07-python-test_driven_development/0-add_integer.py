#!/usr/bin/python3
"""Function that adds 2 integers."""


def add_integer(a, b=98):
    """
    Add two integers.

    Parameters:
    a: int or float
        First integer or float value.
    b: int or float, optional (default=98)
        Second integer or float value.

    Returns:
    int: The addition of 'a' and 'b' as integers.

    Raises:
    TypeError: If 'a' or 'b' is not an integer or float with specific error messages.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
