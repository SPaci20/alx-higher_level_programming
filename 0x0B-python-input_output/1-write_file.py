#!/usr/bin/python3
"""Function that writes a string to a text file."""


def write_file(filename="", text=""):
    """"Use with and returns the number of characters written."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_chars_written = file.write(text)
        return num_chars_written
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
