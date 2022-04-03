#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk


def create_window():

	global window

	window = tk.Tk()
	window.title('combo box practice')
	window.geometry('500x300')

def create_widgets():

	global age_label, prompt_label, name_text, name, click_button, greet_label, age, numberChosen

	#enter name label
	prompt_label = ttk.Label(window, text = 'Enter a name: ')
	prompt_label.grid(column = 0, row = 0)

	#greet label- doesn't show text until button
	#experience click event
	greet_label = ttk.Label(window, text = '')
	greet_label.grid(column = 1, row = 3)
	
	#the string variable that will store the text entered
	name = tk.StringVar()
	name_text = ttk.Entry(window, width = 12, textvariable = name)
	name_text.grid(column = 0, row = 1)

	#click me button that will display the text
	click_button = ttk.Button(window, text = 'click me', command = greet)
	click_button.grid(column = 2, row = 1)

	#combo box- age label and age StringVar
	age_label = ttk.Label(window, text = 'Age:').grid(column = 1, row = 0)
	age = tk.StringVar()
	numberChosen = ttk.Combobox(window, width = 12, textvariable = age, state = 'readonly')
	numberChosen['values'] = (25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35)
	numberChosen.grid(column = 1, row = 1)
	numberChosen.current(0)
	

	name_text.focus()

def greet():

	greet_label.configure(text = 'Hello ' + name.get() + ', you are ' + age.get() + ' years old.')

def run():

	create_window()
	create_widgets()
	window.mainloop()

def main():

	run()	

if __name__ == '__main__':
	main()
