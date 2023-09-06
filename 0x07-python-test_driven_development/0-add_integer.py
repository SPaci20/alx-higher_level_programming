#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    :param a: The first integer.
    :param b: The second integer (default is 98).
    :return: The addition of a and b as an integer.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b
