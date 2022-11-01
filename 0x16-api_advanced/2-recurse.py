#!/usr/bin/python3
"""Module contains a function that queries
the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """function queries the Reddit API and
    returns a list containing the titles of all
    hot articles for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return None
    r = requests.get("https://www.reddit.com/r/{}/hot.json"
                     .format(subreddit),
                     headers={"User-Agent": "Custom-User-Agent"},
                     allow_redirects=False,
                     params={"count": count, "after": after})
    if r.status_code >= 400:
        return None

    after = r.json().get('data').get('after')
    count = r.json().get('data').get('count')

    hot_list2 = hot_list + [post.get("data").get("title")
                            for post in r.json()
                            .get("data")
                            .get("children")]

    if after is None:
        return hot_list2

    return recurse(subreddit, hot_list2, count, after)
