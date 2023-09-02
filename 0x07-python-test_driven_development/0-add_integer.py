def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If `a` is not an integer or `b` is not an integer.

    Returns:
        int: The sum of `a` and `b`.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer or a float")
        else:
            raise TypeError("b must be an integer or a float")

    # Cast a and b to integers if they are floats
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    # Perform the addition and return the result
    return a + b
