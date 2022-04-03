#!/usr/bin/env python
from os import environ
import tweepy

CREDS = environ

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CREDS['TEST_API_KEY'], CREDS['TEST_API_KEY_SECRET'])
    auth.set_access_token(CREDS['TEST_ACCESS_TOKEN'], CREDS['TEST_ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)

    peer = "imm0rtal_0bject"

    try:
        api.create_friendship(peer)
    except Exception as e: print(f"[x] Error: {e}")
    else: print(f"Now following {peer}!")