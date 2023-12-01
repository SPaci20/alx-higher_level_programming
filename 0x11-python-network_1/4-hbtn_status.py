#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
using package requests.
"""

import requests


def fetch_status():
    """
    Sends a GET request to https://intranet.hbtn.io/status
    and prints information about the response.
    """
    try:
        response = requests.get("https://intranet.hbtn.io/status")
        response.raise_for_status()  # Raises HTTPError for bad responses
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    fetch_status()
