#!/usr/bin/env python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Simple():
        
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
                
class Html_Message(Simple):
        
        def __init__(self, sender, recipient, password, subject, text, html):
                
                Simple.__init__(self, sender, recipient, password, subject, text)
                self.html = html
                
        def send_mail(self):
                
                SMTP_INFO = {
                        'host': 'smtp.gmail.com',
                        'port': 587,
                        'username': self.sender,
                        'password': self.password
                }
                
                SENDER_NAME = 'SYSTEM'
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
                        
                        #encrypt the connection
                        smtp.starttls()
                        
                        #Logging in and sending the email:
                        smtp.login(SMTP_INFO['username'], SMTP_INFO['password'])
                        smtp.send_message(message)