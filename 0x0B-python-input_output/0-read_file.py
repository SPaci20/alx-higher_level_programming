#!/usr/bin/python3
"""Function that reads a text file."""


def read_file(filename=""):
    """read text and print it to sdtout using with"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except Exception as e:
        print(f"An error occurred: {e}")
