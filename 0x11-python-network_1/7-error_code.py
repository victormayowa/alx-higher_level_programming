#!/usr/bin/python3
"""Sends a request to a URL and displays the body of the response."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad status codes
        print(response.text)
    except requests.exceptions.HTTPError as err:
        print("Error code: {}".format(err.response.status_code))
