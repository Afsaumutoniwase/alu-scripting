#!/usr/bin/python3
"""0-subs.py"""

import requests
def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0'}  # Setting a custom User-Agent
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
    return 0
