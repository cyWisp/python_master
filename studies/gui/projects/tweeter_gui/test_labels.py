#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk
import time

def main():

	global window, label, beg, mid, end

	window = tk.Tk()
	window.title('test')
	window.geometry('300x50')


	beg = tk.StringVar()
	beg.set('Beginning')

	mid = tk.StringVar()
	mid.set('middle')
	
	end = tk.StringVar()
	end.set('end')

	label = ttk.Label(window, text = beg.get())
	label.grid(column = 0, row = 0)
	window.update()
	
	time.sleep(3)
	label.configure(text = mid.get())
	window.update()
	
	time.sleep(3)
	label.configure(text = end.get())
	window.update()
	
	window.mainloop()	

if __name__ == '__main__':
	main()
