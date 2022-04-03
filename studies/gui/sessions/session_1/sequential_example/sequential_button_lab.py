#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def main():

	#create the window, define title and dimensions
	window = tk.Tk()
	window.title("Sequential")
	window.minsize(width = 500, height = 300)
	window.maxsize(width = 600, height = 800)
	
	#adding a label, giving it a title, and placement
	label_1 = ttk.Label(window, text = "Label 1")
	label_1.grid(column = 0, row = 0)
	
	#button click event callback function
	def click():
		#change the button text to read 'Clicked!'
		action.configure(text = "*** Clicked! ***")
		#change the foreground color of the label to red
		label_1.configure(foreground = 'red')

	#create the button, add text and functionality (command)
	action = ttk.Button(window, text = "Click ME!", command = click)
	#place the button below the label
	action.grid(column = 0, row = 1)
	


	window.mainloop()

if __name__=='__main__':
	main()
