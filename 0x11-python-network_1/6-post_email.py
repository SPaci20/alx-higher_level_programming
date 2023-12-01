#!/usr/bin/python3
"""A script that:
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
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            x_request_id = dict(response.headers).get("X-Request-Id")
            print(x_request_id)
    except URLError as e:
        print(f"Error: {e.reason}")
    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
