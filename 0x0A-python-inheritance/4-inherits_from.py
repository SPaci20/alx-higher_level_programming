#!/usr/bin/python3
"""Define a class inherited-checking(director indirect)."""


def inherits_from(obj, a_class):
    """Check if the object's class inherited (directly or indirectly)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
