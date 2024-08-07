#!/usr/bin/python3
"""
Module 10-my_github
Takes your GitHub credentials (username and password/personal access token)
and uses the GitHub API to display your id.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
