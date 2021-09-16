#!/usr/bin/env python
from os import environ
import tweepy

CREDS = environ

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CREDS['TEST_API_KEY'], CREDS['TEST_API_KEY_SECRET'])
    auth.set_access_token(CREDS['TEST_ACCESS_TOKEN'], CREDS['TEST_ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)

    python_search = api.search(
        q="Mike Lee",
        lang="en",
        rpp=10,
    )

    for tweet in python_search:
        print(f"User: {tweet.user.name}\nTweet: {tweet.text}\n")
    