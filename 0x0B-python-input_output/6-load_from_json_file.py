#!/usr/bin/python3
"""function that creates an Object from a JSON file."""


import json


def load_from_json_file(filename):
    """Use with and json to read the contents of the file and convert it."""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
