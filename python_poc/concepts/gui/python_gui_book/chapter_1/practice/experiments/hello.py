#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def hello_person():
    
    hello_label.configure(text="{0} is {1} years old...".format(str(name.get()), str(age.get())), foreground="red")

if __name__ == '__main__':
    
    window = tk.Tk()
    window.title('Hello ^^')
    window.minsize(height=200, width=200)
    window.resizable(False, False)

    top_label = ttk.Label(window, text="What's your name?").grid(column=0, row=0)
    hello_label = ttk.Label(window, text="")
    hello_label.grid(column=0, row=2)

    name = tk.StringVar()
    name_box = ttk.Entry(window, width=12, textvariable=name).grid(column=0, row=1)

    age = tk.StringVar()
    age_combo = ttk.Combobox(window, width=12, textvariable=age, state="readonly")
    age_combo.grid(column=1, row=1)
    age_combo['values'] = (23, 24, 35, 32, 54)
    age_combo.current(0)

    hello_button = ttk.Button(window, text='Greet', command = hello_person)
    hello_button.grid(column=2, row=1)

    window.mainloop()