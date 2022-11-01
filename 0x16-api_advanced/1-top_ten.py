#!/usr/bin/python3
"""Module contains a function that queries
the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """function queries the Reddit API and
    prints the titles of the first 10
    hot posts listed for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        print('None')
    r = requests.get("https://www.reddit.com/r/{}/hot.json?"
                     .format(subreddit),
                     headers={"User-Agent": "Custom-User-Agent"},
                     allow_redirects=False,
                     params={'limit': 10})
    if r.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in r.json().get("data").get("children")]
