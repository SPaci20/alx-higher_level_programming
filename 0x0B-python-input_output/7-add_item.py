#!/usr/bin/python3
import sys
import json


filename = 'add_item.json'


def load_or_create_list(filename):
    try:
        return load_from_json_file(filename)
    except FileNotFoundError:
        return []


my_list = load_or_create_list(filename)


my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)

# Print the updated list
print(my_list)
