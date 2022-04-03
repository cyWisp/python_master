#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

COLOR_1 = 'Red'
COLOR_2 = 'Green'
COLOR_3 = 'Blue'

def radio_func():

	global radio_selected
	radio_selected = radio_var.get()
	
	if radio_selected == 1:
		label_1.configure(text = 'radio_1 selected')
		window.configure(background = COLOR_1)
	elif radio_selected == 2:
		label_1.configure(text = 'radio_2 selected')
		window.configure(background = COLOR_2)
	elif radio_selected == 3:
		label_1.configure(text = 'radio_3 selected')
		window.configure(background = COLOR_3)


def create_gui():

	global window, label_1, radio_1, radio_2, radio_3, radio_var

	window = tk.Tk()
	window.title('Radio Buttons...')
	window.geometry('800x600')

	label_1 = ttk.Label(window, text = '')
	label_1.grid(column = 0, row = 1, sticky = tk.W)

	radio_var = tk.IntVar()
	radio_1 = tk.Radiobutton(window, variable = radio_var, value = 1, command = radio_func)
	radio_1.grid(column = 0, row = 5, sticky = tk.S)

	radio_2 = tk.Radiobutton(window, variable = radio_var, value = 2, command = radio_func)
	radio_2.grid(column = 1, row = 5, sticky = tk.S)

	radio_3 = tk.Radiobutton(window, variable = radio_var, value = 3, command = radio_func)
	radio_3.grid(column = 3, row = 5, sticky = tk.S)
	
	window.mainloop()

def main():

	create_gui()

if __name__ == '__main__':
	main()
