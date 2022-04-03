#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk
import tweepy, time
from datetime import datetime

def tAuth():
	
	CONSUMER_KEY = 'l0dEuCbwQj2lkPv8lCqekyFPI'
	CONSUMER_SECRET = 'AQ4uIA5kPme7aYQYZB6US15Q88eCWU7097Q3BoN1qgGsISZTlg'
	ACCESS_KEY = '900734602523947008-QYCYixLyJ2IKoDjyIXPqlSCC8KO0Meu' 	
	ACCESS_SECRET =  'Gh2JEmYGjlvVgHQyFO3kejl7LqZrsNC9STtBpzLECvlpI'
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)

	return api
	
def createGui():

	global window, tweet_box, tweet_text, text_label, message_label, submit_button

	window = tk.Tk()
	window.title('miniTweeter')
	window.minsize(width = 800, height = 75)
	window.maxsize(width = 800, height = 75)

	#tweet content label and textbox
	text_label = ttk.Label(window, text = 'Tweet Content:').grid(column = 0, row = 0)
	tweet_text = tk.StringVar()
	tweet_box = ttk.Entry(window, width = 48, textvariable = tweet_text)
	tweet_box.grid(column = 1, row = 0)

	#message label
	message_label = ttk.Label(window, text = 'Ready...')
	message_label.grid(column = 1, row = 1)

	#submit button
	submit_button = ttk.Button(window, text = 'Submit Tweet', command = submit)
	submit_button.grid(column = 5, row = 0)

	tweet_box.focus()

def submit():

	tweetApi = tAuth()
	current_time  = str(datetime.now())
	format_tweet = str(tweet_text.get())
	tweetApi.update_status(format_tweet)

	message_label.configure(text = 'Tweet posted at ' + current_time)
	window.update()
	time.sleep(2)
	
	message_label.configure(text = 'Ready...')
	tweet_box.delete(0, 280)
	window.update()
	
	tweet_box.focus()

def run():

	createGui()
	window.mainloop()
	
def main():	

	run()

if __name__ == '__main__':
	main()
