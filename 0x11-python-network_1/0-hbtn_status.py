#!/usr/bin/python3
"""
Script that:
- fetches https://alx-intranet.hbtn.io/status.
- uses urllib package
"""

import urllib.error
import urllib.request

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(
                'https://alx-intranet.hbtn.io/status'
                ) as res:
            content = res.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
