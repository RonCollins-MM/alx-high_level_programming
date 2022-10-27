#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends
a POST  request to the passed URL with the email as a parameter,
and finally displays the body of the response.
Uses ``requests.posts()`` method
"""
import requests
from sys import argv

if __name__ == "__main__":
    values = {
        'email': argv[2]
    }
    response = requests.post(argv[1], data=values)
    print(response.text)
