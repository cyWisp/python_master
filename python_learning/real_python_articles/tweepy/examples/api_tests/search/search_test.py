#!/usr/bin/env python
from os import environ
import tweepy

CREDS = environ

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CREDS['TEST_API_KEY'], CREDS['TEST_API_KEY_SECRET'])
    auth.set_access_token(CREDS['TEST_ACCESS_TOKEN'], CREDS['TEST_ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)

    io_tweets = api.user_timeline("imm0rtal_0bject", count=10)

    for t in io_tweets:
        print(t.text)
