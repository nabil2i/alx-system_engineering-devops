#!/usr/bin/python3
"""Module contains a function that queries
the Reddit API and returns the number of subs
for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function queries the Reddit API and 
    returns the number of subs for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if r.status_code >= 300:
        return 0

    return r.json().get("data").get("subscribers")
