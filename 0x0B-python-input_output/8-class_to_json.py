#!/usr/bin/python3
"""function that returns the dictionary description."""


def class_to_json(obj):
    """initializes an empty dictionary."""
    serialized_obj = {}
    for attr_name in dir(obj):
        if not attr_name.startswith('_'):
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                serialized_obj[attr_name] = attr_value
    return serialized_obj
