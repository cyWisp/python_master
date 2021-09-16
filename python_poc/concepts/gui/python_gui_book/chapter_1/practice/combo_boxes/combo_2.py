#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def greet():
    
    global name, age
    output_label.configure(text='{0} is {1} years old...'.format(str(name.get()), str(age.get())))

if __name__ == '__main__':
    
    global name, age

    window = tk.Tk()
    window.title('more practice with combo boxes')
    window.minsize(height=300, width=300)

    name_label = ttk.Label(window, text='name:')
    name_label.grid(column=0, row=0)

    age_label = ttk.Label(window, text='age:')
    age_label.grid(column=1, row=0)

    name = tk.StringVar()
    name_text = ttk.Entry(window, width=12, textvariable = name)
    name_text.grid(column=0, row=1)

    age = tk.StringVar()
    age_text = ttk.Combobox(window, width=12, textvariable = age, state='readonly')
    age_text['values'] = (18, 19, 20, 30, 31, 32, 33)
    age_text.current(0)
    age_text.grid(column=1, row=1)

    greet_button = ttk.Button(window, text='Greet', command=greet)
    greet_button.grid(column=2, row=1)

    output_label = ttk.Label(window, text='')
    output_label.grid(column=0, row=2)

    window.mainloop()



