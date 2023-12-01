#!/usr/bin/python3
"""
A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Define the payload with the email parameter
    payload = {'email': email}

    # Send a POST request
    response = requests.post(url, data=payload)

    # Display the body of the response
    print("Your email is:", response.text)
