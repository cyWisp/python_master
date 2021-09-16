#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def main():

	window = tk.Tk()
	window.title("text box adventures")
	window.minsize(width = 500, height = 300)
	window.maxsize(width = 800, height = 600)

	
	name_label = ttk.Label(window, text = "Enter your name:")
	name_label.grid(column = 3, row = 3)

	hello_label = ttk.Label(window, text = "")
	hello_label.grid(column = 3, row = 1)

	name = tk.StringVar()
	nameEntered = ttk.Entry(window, width = 12, textvariable = name)
	nameEntered.grid(column = 4, row = 3)

	def hello_click():
		hello_label.configure(text = "Hello " + name.get())
	
	hello_button = ttk.Button(window, text = "Say Hello!", command = hello_click)
	hello_button.grid(column = 3, row = 5)


	window.mainloop()

if __name__ == '__main__':
	main()
