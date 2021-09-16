#!/usr/bin/env python
from os import environ
import tweepy

CREDS = environ

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CREDS['API_KEY'], CREDS['API_KEY_SECRET'])
    auth.set_access_token(CREDS['ACCESS_TOKEN'], CREDS['ACCESS_TOKEN_SECRET'])

    api = tweepy.API(auth)
    time_line = api.home_timeline()

    for tweet in time_line:
        print(f"{tweet.user.name} said: {tweet.text}")