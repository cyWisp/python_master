#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def calc():
    
    global height, width

    perimeter = (int(height.get()) * 2) + (int(width.get()) * 2)
    result.configure(text='The perimeter is: ' + str(perimeter))

if __name__ == '__main__':
    
    global height, width

    window = tk.Tk()
    window.title('just another experiment')
    window.minsize(height=120, width=200)

    height_label = ttk.Label(window, text='height: ')
    height_label.grid(column=0, row=0)

    height = tk.IntVar()
    height_text = ttk.Entry(window, width=8, textvariable=height)
    height_text.grid(column=1, row=0)

    width_label = ttk.Label(window, text='width: ')
    width_label.grid(column=0, row=1)
    
    width = tk.IntVar()
    width_text = ttk.Entry(window, width=8, textvariable=width)
    width_text.grid(column=1, row=1)

    result = tk.Label(window, text='')
    result.grid(column=1, row=2)

    calc_button = tk.Button(window, text='Calculate', command=calc)
    calc_button.grid(column=0, row=2)

    height_text.focus()

    window.mainloop()
