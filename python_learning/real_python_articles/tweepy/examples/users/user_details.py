#!/usr/bin/env python
from os import environ
import tweepy

CREDS = environ

if __name__ == '__main__':

    auth = tweepy.OAuthHandler(CREDS['TEST_API_KEY'], CREDS['TEST_API_KEY_SECRET'])
    auth.set_access_token(CREDS['TEST_ACCESS_TOKEN'], CREDS['TEST_ACCESS_TOKEN_SECRET'])

    api = tweepy.API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True,
    )

    user = api.get_user("cyWisp_AI")

    print("User Details:")
    print(f"Username: {user.name}\nDescription: {user.description}")
    print(f"Location: {user.location}")

    