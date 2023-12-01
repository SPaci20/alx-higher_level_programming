#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
using package requests.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    # Display information about the response
    print("Body response:")
    print(f"    - type: {type(response.text)}")
    print(f"    - content: {response.text}")
