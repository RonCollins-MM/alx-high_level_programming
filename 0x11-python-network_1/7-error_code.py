#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
If error code is returned, it is extracted from ``response.status_code``
"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    code = response.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(resp.text)
