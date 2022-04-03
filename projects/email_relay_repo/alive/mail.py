#!/usr/bin/env python
import os, sys, smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Html_Message():#======================================================================
        
        def __init__(self, sender, recipient, subject, text, html):
                
                self.sender = sender
                self.recipient = recipient
                self.subject = subject
                self.text = text      
                self.html = html
                
        def send_mail(self):
                
                SMTP_INFO = {
                        'host': 'somerelay.somewhere.com',
                        'port': 25,
                        'username': self.sender,
                }
                
                SENDER_NAME = 'YOUR REPORT'
                RECIPIENT = self.recipient
                SUBJECT = self.subject
                BODY_PLAIN_TEXT = self.text
                BODY_HTML = self.html
                
                message = MIMEMultipart('alternative')
                message['From'] = '{} <{}>'.format(SENDER_NAME, SMTP_INFO['username'])
                message['To'] = RECIPIENT
                message['Subject'] = SUBJECT
                
                #Adding the plain text email body
                message.attach(MIMEText(BODY_PLAIN_TEXT, 'plain'))
                
                #Adding the HTML email BODY_HTML
                message.attach(MIMEText(BODY_HTML, 'html'))
                
                #SMTP server connection
                with smtplib.SMTP(SMTP_INFO['host'], SMTP_INFO['port']) as smtp:
                        smtp.send_message(message)