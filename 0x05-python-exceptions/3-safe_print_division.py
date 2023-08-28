#!/usr/bin/python3

def safe_print_division(a, b):
    """function that divides 2 integers and prints the result.
    Args:
        integers a and b
    Returns: value of the division, otherwise: None
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
