#!/usr/bin/env python
import os, sys, smtplib, time
import tkinter as tk
from tkinter import ttk
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MailMessage():

    def __init__(self, sender, recipient, subject, text):

        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.text = text

    def send_mail(self):

        message = 'Subject: {}\n\n{}'.format(self.subject, self.text)
        server_connect = smtplib.SMTP('your.internal.relay')
        server_connect.sendmail(self.sender, self.recipient, message)

def send_message():

    sender = str(sender_text_var.get())
    recipient = str(recipient_text_var.get())
    subject = str(subject_text_var.get())
    body = str(body_text_box.get("1.0", 'end-1c'))

    mail_message = MailMessage(sender, recipient, subject, body)
    mail_message.send_mail()

    time.sleep(3)
    sent_label.configure(text='Message Sent!', foreground='red')
    master.update()
    time.sleep(3)
    clear_fields()

def clear_fields():

    sender_text_box.delete(0, 'end')
    recipient_text_box.delete(0, 'end')
    subject_text_box.delete(0, 'end')
    body_text_box.delete('1.0', 'end')

    sent_label.configure(text='Ready...', foreground='black')
    master.update()

def exit_app():

    sys.exit(0)

if __name__ == '__main__':

    global master
    master = tk.Tk()
    master.minsize(width=350, height=300)
    master.title('sP00fz')

    #text variables
    global sender_text_var, recipient_text_var, subject_text_var, sent_label

    #text_fields
    global sender_text_box, recipient_text_box, subject_text_box, body_text_box

    #start widgets=================================================

    title_label = ttk.Label(master, text='sP00fz')
    title_label.grid(column=1, row=0)

    #sender========================================================

    sender_label = ttk.Label(master, text='Sender:')
    sender_label.grid(column=0, row=1)

    sender_text_var = tk.StringVar()
    sender_text_box = ttk.Entry(master, width = 39, textvariable = sender_text_var)
    sender_text_box.grid(column=1, row=1, sticky='W', pady=3)

    #==============================================================

    recipient_label = ttk.Label(master, text='Recipient:')
    recipient_label.grid(column=0, row=2)

    recipient_text_var = tk.StringVar()
    recipient_text_box = ttk.Entry(master, width = 39, textvariable = recipient_text_var)
    recipient_text_box.grid(column=1, row=2, sticky='W', pady=3)

    #==============================================================

    subject_label = ttk.Label(master, text='Subject:')
    subject_label.grid(column=0, row=3)

    subject_text_var = tk.StringVar()
    subject_text_box = ttk.Entry(master, width = 39, textvariable = subject_text_var)
    subject_text_box.grid(column=1, row=3, sticky='W', pady=3)

    #==============================================================

    body_label = ttk.Label(master, text='Body:')
    body_label.grid(column=0, row=4)

    body_text_box = tk.Text(master, width=30, height=10)
    body_text_box.grid(column=1, row=4, sticky='W', pady=3)

    sent_label = ttk.Label(master, text='Ready...')
    sent_label.grid(column=1, row=6, sticky='W', pady=3)

    send_button = ttk.Button(master, text='Send', command=send_message)
    send_button.grid(column=1, row=5, sticky='W', pady=3)

    sent_label = ttk.Label(master, text='Ready...')
    sent_label.grid(column=1, row=6, sticky='W', pady=3)

    exit_button = ttk.Button(master, text='Exit', command=exit_app)
    exit_button.grid(column=1, row=5, pady=3, padx=(168, 0))

    sender_text_box.focus()
    master.mainloop()
