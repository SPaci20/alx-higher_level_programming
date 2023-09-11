#!/usr/bin/python3
def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    :param obj: The object to inspect.
    :return: A list of attribute and method names.
    """
    return dir(obj)
