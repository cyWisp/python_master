#!/usr/bin/env python
from os import environ
import tweepy

CREDS = environ

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CREDS['TEST_API_KEY'], CREDS['TEST_API_KEY_SECRET'])
    auth.set_access_token(CREDS['TEST_ACCESS_TOKEN'], CREDS['TEST_ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)

    tweets = api.home_timeline(count = 1)
    tweet = tweets[0]
    print(f"Liking tweet {tweet.id} of {tweet.author.name}")
    api.create_favorite(tweet.id)