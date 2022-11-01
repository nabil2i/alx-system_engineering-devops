#!/usr/bin/python3
"""Module contains a function that queries
the Reddit API,  parses the title of all hot articles,
and prints a sorted count of given keywords"""

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """function queries the Reddit API,  parses the title
    of all hot articles, and prints a sorted
    count of given keywords"""
    if subreddit is None or type(subreddit) is not str:
        return None
    r = requests.get("https://www.reddit.com/r/{}/hot.json"
                     .format(subreddit),
                     headers={"User-Agent": "Custom-User-Agent"},
                     allow_redirects=False,
                     params={"after": after})
    if r.status_code nis not 200:
        return None

    after = r.json().get('data').get('after')

    hot_list = [post.get("data").get("title")
                for post in r.json()
                .get("data")
                .get("children")]

    if not hot_list:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in hot_list:
        title_words = title.split(' ')
        for word in word_list:
            for title_word in title_words:
                if title_word.lower() == word.lower():
                    word_count[word] += 1

    if not after:
        sorted_counts = sorted(word_count.items(), key=None)
    else:
        return count_words(subreddit, word_list, word_count, after)
