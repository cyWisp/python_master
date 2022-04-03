#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def click_me():

	action.configure(text="**I have been clicked**")
	aLabel.configure(foreground='red')


def main():
	
	global win, aLabel, action

	#create the main window
	win = tk.Tk()
	#modify title of the window
	win.title('adding a label')
	

	#add a label        #label text        #label position
	aLabel = ttk.Label(win, text="just a label")
	aLabel.grid(column=0, row=0)


	#add a button       #parent window  text    #function onclick
	action = ttk.Button(win, text="click me!", command=click_me)
	action.grid(column=1, row=0)




	#window is not resizeable
	win.resizable(0,0)
	
	#start the program and wait for events
	win.mainloop()	

if __name__ == '__main__':
	main()
