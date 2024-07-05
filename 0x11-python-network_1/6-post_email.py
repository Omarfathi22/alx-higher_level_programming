#!/usr/bin/python3
"""
Module 6-post_email
Takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
