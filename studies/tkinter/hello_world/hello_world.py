#!/usr/bin/env python
from tkinter import *
import sys

def exit_app():

	sys.exit(0)

if __name__ == '__main__':

	root = Tk()
	root.minsize(width=200, height=200)

	hello_label = Label(root, text='Hello, Rob!').pack(side=TOP)
	big_button = Button(root, text='Big Button', pady=30, padx=30, fg='red', bg='black').pack(side=LEFT)
	exit_button = Button(root, text='Exit', fg='red', bg='blue', command=exit_app).pack(side=BOTTOM)

	root.mainloop()
