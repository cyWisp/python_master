#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def check_values():
    
    value_1 = str(chk_1.get())
    value_2 = str(chk_2.get())
    value_3 = str(chk_3.get())
    
    if value_1 == 1:
        value_label.configure(text='current values: {0} | {1} | {2}'.format(value_1, value_2, value_3))

if __name__ == '__main__':

    window = tk.Tk()
    window.title('Playing with check buttons')
    window.minsize(height=200, width=200)
    window.resizable=(False, False)

    #top label
    top_label = ttk.Label(window, text='Check Buttons').grid(column=0, row=0)

    #check buttons
    global chk_1, chk_3, chk_3

    chk_1 = tk.IntVar()
    chk_2 = tk.IntVar()
    chk_3 = tk.IntVar()

    chk_button_1 = tk.Checkbutton(window, text='first', variable=chk_1)
    chk_button_2 = tk.Checkbutton(window, text='second', variable=chk_2)
    chk_button_3 = tk.Checkbutton(window, text='third', variable=chk_3)

    chk_button_1.grid(column=0, row=1)
    chk_button_2.grid(column=1, row=1)
    chk_button_3.grid(column=2, row=1)

    check_button = ttk.Button(window, text='check', command=check_values)
    check_button.grid(column=0, row=2)

    value_label = ttk.Label(window, text='')
    value_label.grid(column=1, row=2)

    if_label = ttk.Label(window, text='')
    if_label.grid(column=1, row=3)

    window.mainloop()