#!/usr/bin/env python
from tkinter import *
import sys

def exit_app():

    sys.exit(0)

if __name__ == '__main__':

    root = Tk()
    root.minsize(width=300, height=300)

    names = ['Rob', 'Dan', 'Mike']

    for index, name in enumerate(names):

        index += 1
        new_name = Label(root, text='{0}. Hello {1}'.format(str(index), name))
        new_name.pack()

    new_button = Button(root, text='Exit', command=exit_app)
    new_button.pack()

    root.mainloop()