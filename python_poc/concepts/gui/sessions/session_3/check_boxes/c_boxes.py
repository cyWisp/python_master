#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def main():

	#create main window
	window = tk.Tk()
	window.title('check boxes')
	window.minsize(width = 500, height = 300)
	window.maxsize(width = 800, height = 600)

	#creating three labels

	left_label = ttk.Label(window, text = 'Left label').grid(column = 0, row = 0)
	middle_label = ttk.Label(window, text = 'Middle label').grid(column = 1, row = 0)
	right_label = ttk.Label(window, text = 'Right label').grid(column = 2, row = 0)

	#create three check boxes
	check_1_var = tk.IntVar()
	check_1 = tk.Checkbutton(window, text = "Disabled", variable = check_1_var, state = 'disabled')
	check_1.select()
	check_1.grid(column = 0, row = 2, stick=tk.W) #

	#
	check_2_var = tk.IntVar()
	check_2 = tk.Checkbutton(window, text = "Unchecked", variable = check_2_var)
	check_2.deselect()
	check_2.grid(column = 1, row = 2)

	#
	check_3_var = tk.IntVar()
	check_3 = tk.Checkbutton(window, text = 'Enabled', variable = check_3_var)
	check_3.select()
	check_3.grid(column = 2, row = 2)


	window.mainloop()

if __name__ == '__main__':
	main()
