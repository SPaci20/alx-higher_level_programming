#!/usr/bin/python3
""" function that writes an Object to a text file, using a JSON."""


import json


def save_to_json_file(my_obj, filename):
    """Use with and Represent the JSON."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
