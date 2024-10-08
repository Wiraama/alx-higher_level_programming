#!/usr/bin/python3
""" script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == '__main__':
    url = "https://api.github.com/user"

    res = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    if res.status_code == 200:
        info = res.json()
        print(info.get("id"))
    else:
        print("None")
