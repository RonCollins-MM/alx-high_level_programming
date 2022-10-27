#!/usr/bin/python3
"""
Python script that list 10 commits
(from the most recent to oldest) of the repository
"""

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            sha = commits[i].get('sha')
            auth_name = commits[i].get('commit').get('author').get('name')
            print(f'{sha}: {auth_name}')
    except IndexError:
        pass
