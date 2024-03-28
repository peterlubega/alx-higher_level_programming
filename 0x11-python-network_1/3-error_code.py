#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
