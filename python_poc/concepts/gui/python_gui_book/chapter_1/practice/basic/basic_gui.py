#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def click_me():
    
    label_1.configure(text='button has been clicked!', foreground='red')

if __name__ =='__main__':
    
    window = tk.Tk()
    window.title('This is just some more practice')

    label_1 = ttk.Label(window, text='Practice label...')
    label_1.grid(column=0, row=0)

    button_1 = ttk.Button(window, text='click me!', command=click_me)
    button_1.grid(column=0, row=1)

    window.mainloop()

    
