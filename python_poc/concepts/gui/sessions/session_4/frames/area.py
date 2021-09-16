#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

#this application calculates the area of a rectangle


def calculate():

	try:
		l = int(length.get())
		w = int(width.get())
		area.set(l * w)
	except ValueError:
		pass

def create_gui():
	
	#============ variables declarations ============
	
	#declare global variables for window, frames, widgets
	global root, mainframe, length, width, area, length_entry, width_entry, length_label, width_label, area_label, area_result, calc_button

	#============ main window and frame ============

	#create the main window
	root = tk.Tk()
	root.title('Area Caclulator')

	#create the main frame and place it within the window
	mainframe = ttk.Frame(root, padding = "3 3 12 12")
	mainframe.grid(column = 0, row = 0, sticky = ('N, W, E, S'))
	mainframe.columnconfigure(0, weight = 1)
	mainframe.rowconfigure(0, weight = 1)

	#============ variable definitions ============

	#define string variables for operations
	length = tk.StringVar()
	width = tk.StringVar()
	area = tk.StringVar()

	#============ widgets ============

	length_entry = ttk.Entry(mainframe, width = 7, textvariable = length)
	length_entry.grid(column = 2, row = 1, sticky = ('W, E'))

	width_entry = ttk.Entry(mainframe, width = 7, textvariable = width)
	width_entry.grid(column = 2, row = 2, stick = ('W, E'))

	length_label = ttk.Label(mainframe, text = 'Length: ')
	length_label.grid(column = 1, row = 1, sticky = 'e')

	width_label = ttk.Label(mainframe, text = 'Width: ')
	width_label.grid(column = 1, row = 2, sticky = 'e')

	area_label = ttk.Label(mainframe, text = 'Area: ')
	area_label.grid(column = 1, row = 3, sticky = 'e')

	area_result = ttk.Label(mainframe, text = 'None', textvariable = area)
	area_result.grid(column = 2, row = 3, sticky = ('W, E'))

	calc_button = ttk.Button(mainframe, text = 'Calculate', command = calculate)
	calc_button.grid(column = 3, row = 3, stick = 'w')

	#============ unified widget formatting ============
	
	for child in mainframe.winfo_children():
		child.grid_configure(padx = 5, pady = 5)

	#============ focus and bindings ============

	length_entry.focus()
	root.bind('<Return>', calculate)

	root.mainloop()

def main():

	create_gui()	

if __name__ == '__main__':
	main()
