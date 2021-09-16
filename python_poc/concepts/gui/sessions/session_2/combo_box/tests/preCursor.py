#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def createWindow():

	global window
	window = tk.Tk()
	window.title('More Practice')
	window.minsize(width = 1000, height = 800)
	window.maxsize(width = 1200, height = 1000)

def get_questions():

	global question
	
	with open('questions.txt', 'r') as qFile:
		question = qFile.read()
	qFile.close()

def createWidgets():

	global questionText, a_button, b_button, c_button, d_button, answer_label

	questionText = tk.Text(window)
	questionText.grid(column = 3, row = 2)
	questionText.insert(0.0, question)


	answer_label = ttk.Label(window, text = '')
	answer_label.grid(column = 3, row = 5)


	a_button = ttk.Button(window, text = 'A', command = btn_A).grid(column = 1, row = 3)
	b_button = ttk.Button(window, text = 'B', command = btn_B).grid(column = 2, row = 3)
	c_button = ttk.Button(window, text = 'C', command = btn_C).grid(column = 3, row = 3)
	d_button = ttk.Button(window, text = 'D', command = btn_D).grid(column = 4, row = 3)

	
def btn_A():
	answer_label.configure(text = 'Correct!')
def btn_B():
	answer_label.configure(text = 'Incorrect!')
def btn_C():
	answer_label.configure(text = 'Incorrect!')
def btn_D():
	answer_label.configure(text = 'Incorrect!')
def run():
	
	get_questions()
	createWindow()
	createWidgets()

	window.mainloop()

def main():

	run()

if __name__ == '__main__':
	main()
