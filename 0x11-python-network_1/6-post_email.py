#!/usr/bin/python3
"""
A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request
from urllib.error import URLError, HTTPError

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Create a request object
        request = urllib.request.Request(url)

        # Send the request and get the response
        with urllib.request.urlopen(request) as response:
            # Access the X-Request-Id header using get to avoid exceptions
            x_request_id = dict(response.headers).get("X-Request-Id")
            print(x_request_id)
    except (URLError, HTTPError) as e:
        print(f"Error: {e}")
