#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses

        print(response.text)
    except requests.RequestException as e:
        print(f"Error: {e}")
