#!/usr/bin/python3
"""
Script that:
- takes in a URL, sends a request to the URL, displays response
-HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
-You must use the packages requests and sys
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    # Display the body of the response
    print(response.text)

    # Check if the HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)
