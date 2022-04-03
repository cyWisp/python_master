#!/usr/bin/env python
from os import environ
import tweepy
from sys import argv

if __name__ == '__main__':
	creds = environ

	# authenticate to twitter
	auth = tweepy.OAuthHandler(creds['API_KEY'], creds['API_KEY_SECRET'])
	auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])

	# Create an API object
	api = tweepy.API(auth)

	# Post a tweet
	api.update_status(argv[1])
