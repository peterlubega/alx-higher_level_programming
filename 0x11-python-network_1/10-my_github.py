#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication with a personal access token as password.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    url = "https://api.github.com/user"
    r = requests.get(url, auth=auth)
    if r.status_code == 200:
        print(r.json().get("id"))
    else:
        print(None)
