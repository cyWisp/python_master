#!/usr/bin/env python
import tweepy
from os import environ

if __name__ == '__main__':
    creds = environ

    auth = tweepy.OAuthHandler(creds['TEST_API_KEY'], creds['TEST_API_KEY_SECRET'])
    auth.set_access_token(creds['TEST_ACCESS_TOKEN'], creds['TEST_ACCESS_TOKEN_SECRET'])

    api = tweepy.API(auth)

    try: api.verify_credentials()
    except Exception as e: print(f"[x] Error: {e}")
    else: print("[+] Authentication Succeeded!")
