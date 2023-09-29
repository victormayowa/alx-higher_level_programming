#!/usr/bin/python3
"""Fetches 10 most recent commits from a GitHub repository."""
import requests
import sys


if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    params = {"per_page": 10}

    response = requests.get(url, params=params)

    try:
        data = response.json()
        for commit in data:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    except ValueError:
        print(None)
