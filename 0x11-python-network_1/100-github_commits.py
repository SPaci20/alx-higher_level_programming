#!/usr/bin/python3
"""
A script that:
- takes 2 arguments: repository name and owner name
- uses the GitHub API to list 10 most recent commits
  from the repository by the specified owner
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository> <owner>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {"per_page": 10}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        commits = response.json()

        for commit in commits:
            sha = commit.get("sha")
            author_info = commit.get("commit", {}).get("author", {})
            author_name = author_info.get("name")
            print(f"{sha}: {author_name}")
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        sys.exit(1)
    except ValueError:
        print("Not a valid JSON")
        sys.exit(1)
