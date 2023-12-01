#!/usr/bin/python3
"""
This script takes in a URL, sends a request, and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Fetches the X-Request-Id value from the header of the response.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The X-Request-Id value or a message if the header is not found.
    """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            return x_request_id
        else:
            return "X-Request-Id header not found in the response."


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    result = fetch_x_request_id(url)
    print(result)
