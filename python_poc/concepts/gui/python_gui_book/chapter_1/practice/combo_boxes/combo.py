#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

def print_info():
    
    global name, age
    output_label.configure(text='Name: {0} | Age: {1}'.format(str(name.get()), str(age.get())))

if __name__ == '__main__':

    global name, age

    window = tk.Tk()
    window.title('combo box practice')
    window.minsize(height=300, width=300)

    greeting = ttk.Label(window, text='Please enter your name and age...')
    greeting.pack()

    name = tk.StringVar()
    name_text = ttk.Entry(window, width=12, textvariable=name)
    name_text.pack()

    age = tk.StringVar()
    age_combo_box = ttk.Combobox(window, width=12, textvariable=age)
    age_combo_box['values'] = (18, 19, 20, 21, 22, 23, 24, 25)
    age_combo_box.pack()
    age_combo_box.current(0)

    echo_info = ttk.Button(window, text='Echo', command=print_info)
    echo_info.pack()

    output_label = ttk.Label(window, text='')
    output_label.pack()

    window.mainloop()


