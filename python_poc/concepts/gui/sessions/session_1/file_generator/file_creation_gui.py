#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk
import sys, os

def main():

	#create the window, size and title
	window = tk.Tk()
	window.title("File Generator")
	window.minsize(width = 500, height = 300)
	window.maxsize(width = 800, height = 600)

	label_1 = ttk.Label(window, text = "Generate File!")
	label_1.grid(column = 3, row = 1)

	def generate_file():
	
		with open('text.txt', 'w+') as testFile:
			testFile.write("Just a test")
		testFile.close()

		action.configure(text = "Done!")
		label_1.configure(foreground = "red", text = "File Generated!")

	action = ttk.Button(window, text = "Generate File", command = generate_file)
	action.grid(column = 3, row = 3)

	window.mainloop()

if __name__ == '__main__':
	main()
