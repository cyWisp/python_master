#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk



def createWindow():

	global window

	window = tk.Tk()
	window.title('another test')
	window.minsize(width = 500, height = 300)
	window.maxsize(width = 800, height  = 600)

def create_widgets():

	global name_label, hello_label, name, hello_button, nameEntered

	name_label = ttk.Label(window, text = 'Enter your name:')
	name_label.grid(column = 3, row = 3)
	
	hello_label = ttk.Label(window, text = '')
	hello_label.grid(column = 3, row = 1)

	#StringVar class within tk - text variable resides within Entry class
	name = tk.StringVar()
	nameEntered = ttk.Entry(window, width = 12, textvariable = name)
	nameEntered.grid(column = 4, row = 3)
	
	#the .focus() method will ensue the cursor appears in 
	#the text box as soon as the application is started
	nameEntered.focus()

	hello_button = ttk.Button(window, text = "Greet", command = clickEvent)
	hello_button.grid(column = 3, row = 5)

	#uncommenting the below line will disable the button widget
	#hello_button.configure(state = 'disabled')

def run():

	createWindow()
	create_widgets()
	window.mainloop()

def clickEvent():
		
	hello_label.configure(text = "Hello " + name.get())
	
def main():

	run()	

if __name__  == '__main__':
	main()
