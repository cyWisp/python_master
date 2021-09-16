#!/usr/bin/env python
import tkinter as tk, os, time
from tkinter import ttk

def ping_host():
    
    ping_button.configure(text='PINGING...')

    command = 'ping -c 4 {0} > temp.txt'.format(str(ip_var.get()))
    os.system(command)

    try:
        with open('./temp.txt', 'r') as output_file:
            for index, line in enumerate(output_file):
                new_label = ttk.Label(window, text=line)
                new_label.grid(column=0, row=index)
                window.update()
                time.sleep(1)
    except:
        print('[x] Something went wrong...')
    finally:
        #cleanup
        output_file.close()
        os.remove('./temp.txt')

    ping_button.configure(text='ping', foreground='black')

if __name__ == '__main__':

    window = tk.Tk()
    window.title('more practice')
    window.minsize(height=200, width=200)

    ip_label = ttk.Label(window, text='Enter an IP address:')
    ip_label.grid(column=0, row=0)
    
    ip_var = tk.StringVar()
    ip_entry = ttk.Entry(window, width=20, textvariable=ip_var)
    ip_entry.grid(column=1, row=0)

    ping_button = ttk.Button(window, text='ping', command=ping_host)
    ping_button.grid(column=2, row=0)


    window.mainloop()