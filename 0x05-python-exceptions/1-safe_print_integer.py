#!/bin/usr/python3

def safe_print_integer(value):
    """ print an integer with "{:d}".format().
    Args: value - Any type (integer,string, etc)
    Returns: True if value has been correclty printed
    other wise return False
    """
    try:
        print("{:d}".format(value))
        return(True)
    except(TypeError, ValueError):
        return(False)
