#!/usr/bin/python3
"""
Script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send a POST request
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the body of the response
        body_content = response.read().decode('utf-8')
        print(body_content)
