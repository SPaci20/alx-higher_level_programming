#!/usr/bin/python3
"""
A script that:
- takes in a URL
- sends a request to the URL
- displays the body of the response.
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
