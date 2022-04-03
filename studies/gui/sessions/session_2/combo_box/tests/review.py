#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def main():


	window = tk.Tk()
	window.title('practice')
	window.minsize(width = 500, height = 300)
	window.maxsize(width = 800, height = 600)
	
	global g_label, q_label, c_label, y_button, n_button

	#using the ttk.Label() class 
	g_label = ttk.Label(window, text = 'Greetings!')
	g_label.grid(column = 3, row = 1)

	q_label = ttk.Label(window, text = 'Do you like programming?')
	q_label.grid(column = 3, row = 3)

	y_button = ttk.Button(window, text = 'Yes', command = yes)
	y_button.grid(column = 2, row = 4)
	
	n_button = ttk.Button(window, text = 'No', command = no)
	n_button.grid(column = 4, row = 4)

	c_label = ttk.Label(window, text = '')
	c_label.grid(column = 3, row = 5)

	window.mainloop()

def yes():
	c_label.configure(text = 'Me too!')
def no():
	c_label.configure(text = "That's too bad :(")
		
	
	

if __name__ == '__main__':
	main()
