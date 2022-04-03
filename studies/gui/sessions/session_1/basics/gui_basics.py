#basic import for tkinter
import tkinter as tk

#widget module (assumption)
from tkinter import ttk

def main():

	#create the window by calling the Tk() class
	window = tk.Tk()

	#sets the window title
	window.title("Python GUI")

	#prevents the window from being resized
	#window.resizable(300,300)

	#this sets the initial size of the window
	#window.geometry("300x300")

	#this can also be used to set the initial size of the window
	#and prevent it from being resized
	window.minsize(width=500, height=300)
	window.maxsize(width=800, height=600)

	num_labels = 5
	label = "label "

	#add a label
	#ttk.Label(window, text="This is a Label").grid(column=0, row=0) #<-- not hard to understand
	
	#this loop populated the form with 5 labels, numbered by the counter variable
	#defined within the loop
	for l in range(0, num_labels):
		ttk.Label(window, text=label+str(l)).grid(column=0,row=l)
		

	#------------------------------------Main Event Loop
	#starts the window's event loop
	window.mainloop()

if __name__ == '__main__':
	main()
