#!/usr/bin/env python
import os, smtplib

class Mailer():

	def __init__(self, sender, recipient, password, subject, text):

		self.sender = sender
		self.password = password
		self.recipient = recipient
		self.subject = subject
		self.text = text

	def send_mail(self):

		message = 'Subject: {}\n\n{}'.format(self.subject, self.text)
		server_connect = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server_connect.ehlo()
		server_connect.login(self.sender, self.password)
		server_connect.sendmail(self.sender, self.recipient, message)
		
