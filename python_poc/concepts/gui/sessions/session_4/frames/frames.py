#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def main():

	global window, content, label_1, label_2, label_3, button_1

	window = tk.Tk()
	window.title('layout practice')
	window.geometry('800x600')

	content = ttk.Frame(window, padding=(3, 3, 12, 12))
	content.grid(column = 0, row = 0)

	label_1 = ttk.Label(content, text = 'this is label 1')
	label_1.grid(column = 0, row = 0)
	
	label_2 = ttk.Label(content, text = 'this is label 2')
	label_2.grid(column = 0, row = 1)

	label_3 = ttk.Label(content, text = 'this is label 3')
	label_3.grid(column = 0, row = 2)

	button_1 = ttk.Button(content, text = 'button 1')
	button_1.grid(column = 0, row = 3)

	window.mainloop()	

if __name__ == '__main__':
	main()
