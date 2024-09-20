#!/usr/bin/python3
""" The Holberton School staff evaluates candidates
applying for a back-end position with multiple technical challenges,
like this one:"""
import sys
import requests

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits"

    res = requests.get(url)

    if res.status_code == 200:
        commits = res.json()[:10]
        for commit in commits:
            sha = commit.get("sha")
            owner = commit.get('commit').get('author').get('name')
            print(f"{sha}: {owner}")
        else:
            print(f"Error {res.status_code}")
