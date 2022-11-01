#!/usr/bin/python3
"""Module contains a function that queries
the Reddit API and returns the number of subs
for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function queries the Reddit API and 
    returns the number of subs for a given subreddit"""
    if subreddit is None of type(subreddit) is not str:
        return 0
    r = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                     allow_redirects=False).json()
    r.headers["User-Agent": "custom user agent"]
    if r.status_code >= 300:
        return 0
    
    return r..get("data").get("subscribers")
