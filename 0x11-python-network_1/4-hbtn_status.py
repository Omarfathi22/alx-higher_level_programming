#!/usr/bin/python3
"""
Module 4-hbtn_status
Fetches https://alx-intranet.hbtn.io/status and displays the body of the response.
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
