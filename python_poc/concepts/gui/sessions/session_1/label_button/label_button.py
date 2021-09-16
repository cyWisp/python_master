#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk


#creating a function for the button click event
def button_click():

	#this will configure the text of the button dynamically
	#to read 'CLICKED' when it is in fact clicked
	action.configure(text="*** CLICKED ***")

	#this will change the foreground color of 'label_1'
	#to red when the button has been clicked
	label_1.configure(foreground='red')

def main():

	#define the window, title, min and max size
	window = tk.Tk()
	window.title("This is another test")
	window.minsize(width = 500, height = 300)
	window.maxsize(width = 800, height = 600)

	

	#add a label- defines the window it is to be added to
	#also defines the text of said label
	global label_1
	label_1 = ttk.Label(window, text = "Label 1")
	#defines the positioning of the label as per the layout manager
	label_1.grid(column = 0, row = 0)

	#adding the button
	global action
	
	action = ttk.Button(window, text = "Click Me!", command = button_click)
	action.grid(column = 0, row = 1)

	window.mainloop()
	

if __name__ == '__main__':
	main()
