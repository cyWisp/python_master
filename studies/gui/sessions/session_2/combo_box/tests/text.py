#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

MAX_HEIGHT = 600
MAX_WIDTH = 800
MIN_HEIGHT = 300
MIN_WIDTH = 500

def main():

	someText = "This is some text"

	window = tk.Tk()
	window.title('practice')
	window.minsize(width = MIN_WIDTH, height = MIN_HEIGHT)
	window.maxsize(width = MAX_WIDTH, height = MAX_HEIGHT)

	#using the text widget
	showText = tk.Text(window)
	showText.grid(column = 1, row = 1)
	showText.insert(0.0, someText)

	window.mainloop()

if __name__ == '__main__':
	main()
