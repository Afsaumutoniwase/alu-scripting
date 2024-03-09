#!/usr/bin/python3
"""
0-subs.py
"""
import requests
def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
    return 0
# Test the function
subreddit = 'learnpython'
subscribers = number_of_subscribers(subreddit)
print(f"The number of subscribers in r/{subreddit} is: {subscribers}")
