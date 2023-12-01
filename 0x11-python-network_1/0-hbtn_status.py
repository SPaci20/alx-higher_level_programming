#!/usr/bin/python3
"""
Script fetches the status of https://alx-intranet.hbtn.io
"""

import urllib.request


def fetch_status(url):
    """
    Fetches the status of the given URL and displays response.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    with urllib.request.urlopen(url) as response:
        # Read the body of the response
        content = response.read()

        # Display information about the response
        print("Body response:")
        print("    - type:", type(content))
        print("    - content:", content)
        print("    - utf8 content:", content.decode('utf-8'))


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_status(url)
