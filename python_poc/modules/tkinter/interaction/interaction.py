#!/usr/bin/env python
from tkinter import *
import sys

def button():
    
	button_1.config(text='clicked')

if __name__ == '__main__':

	global button_1

	root = Tk()
	root.minsize(width=200, height=200)
	
	button_1 = Button(root, text='click_me', command=button)
	button_1.pack()

	root.mainloop()
