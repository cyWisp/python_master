#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

COLOR_1 = "Blue"
COLOR_2 = "Gold"
COLOR_3 = "Red"

def radCall():
    
    radSel = radVar.get()
    if radSel == 1:
        window.configure(background=COLOR_1)
    elif radSel == 2:
        window.configure(background=COLOR_2)
    elif radSel == 3:
        window.configure(background=COLOR_3)

def click_me():
    
    action_button.configure(text='clicked')

if __name__ == '__main__':

    window = tk.Tk()
    window.title('radio boxes')
    #window.minsize(height=200, width=200)

    ttk.Label(window, text='Enter a name:').grid(column=0, row=0)
    ttk.Label(window, text='Choose a number:').grid(column=1, row=0)

    name = tk.StringVar()
    name_text = ttk.Entry(window, width=12, textvariable=name).grid(column=0, row=1)

    num = tk.StringVar()
    num_combo = ttk.Combobox(window, width=12, textvariable=num)
    num_combo.grid(column=1, row=1)
    num_combo['values'] = (1, 2, 3, 4, 5)
    num_combo.current(0)

    action_button = ttk.Button(window, text='click me', command=click_me)
    action_button.grid(column=2, row=1)

    check_var_1 = tk.IntVar()
    check_button_1 = tk.Checkbutton(window, text='Disabled', variable=check_var_1, state='disabled')
    check_button_1.select()
    check_button_1.grid(column=0, row=2, sticky=tk.W)

    check_var_2 = tk.IntVar()
    check_button_2 = tk.Checkbutton(window, text='UnChecked', variable=check_var_2)
    check_button_2.deselect()
    check_button_2.grid(column=1, row=2, sticky=tk.W)

    check_var_3 = tk.IntVar()
    check_button_3 = tk.Checkbutton(window, text='Enabled', variable=check_var_3)
    check_button_3.select()
    check_button_3.grid(column=2, row=2, sticky=tk.W)

    radVar = tk.IntVar()
    rad_1 = tk.Radiobutton(window, text=COLOR_1, variable=radVar, value=1, command=radCall)
    rad_1.grid(column=0, row=4, stick=tk.W, columnspan=3)

    rad_2 = tk.Radiobutton(window, text=COLOR_2, variable=radVar, value=2, command=radCall)
    rad_2.grid(column=1, row=4, stick=tk.W, columnspan=3)

    rad_3 = tk.Radiobutton(window, text=COLOR_3, variable=radVar, value=3, command=radCall)
    rad_3.grid(column=2, row=4, stick=tk.W, columnspan=3)

    

    window.mainloop()
