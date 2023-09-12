#!/usr/bin/python3
"""function that returns an object represented by a JSON string."""


import json


def from_json_string(my_str):
    """Uses json to convert it into a Python object."""
    return json.loads(my_str)
