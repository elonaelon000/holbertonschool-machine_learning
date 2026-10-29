#!/usr/bin/env python3
"""Print a GitHub user's location using the GitHub API."""

import math
import sys
import time

import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = int(response.headers["X-RateLimit-Reset"])
        minutes = max(0, math.ceil((reset_time - time.time()) / 60))
        print("Reset in {} min".format(minutes))
    elif response.status_code == 200:
        print(response.json().get("location"))
