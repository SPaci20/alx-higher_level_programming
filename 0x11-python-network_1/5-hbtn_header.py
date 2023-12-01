#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL, and
displays the value of the variable X-Request-Id in the response header.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    # Access the X-Request-Id header using get to avoid exceptions
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id:
        print(x_request_id)
