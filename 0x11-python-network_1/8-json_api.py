#!/usr/bin/python3
"""A script that:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests
from requests.exceptions import RequestException


if __name__ == "__main__":
    search_letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": search_letter}

    try:
        response = requests.post(
                "http://0.0.0.0:5000/search_user",
                data=payload
                ).json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
    except RequestException as e:
        print(f"Request Error: {e}")
