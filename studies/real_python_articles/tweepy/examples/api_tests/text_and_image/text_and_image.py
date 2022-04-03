#!/usr/bin/env python
from os import environ
import tweepy

CREDS = environ

def authenticate():
    auth = tweepy.OAuthHandler(CREDS['TEST_API_KEY'], CREDS['TEST_API_KEY_SECRET'])
    auth.set_access_token(CREDS['TEST_ACCESS_TOKEN'], CREDS['TEST_ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)
    
    return api

if __name__ == '__main__':
    api = authenticate()

    image_path = "./purpose.jpg"
    status = "Seek his purpose!"

    api.update_with_media(image_path, status)
