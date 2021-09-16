from tkinter import *
from tkinter import ttk

#calculate function
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk() #create the root window
root.title("Feet to Meters") #give the root window a title

#create the main frame and place it within the root window
mainframe = ttk.Frame(root, padding="3 3 12 12") #parameters include parents window and padding
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #positing - sticky centering ** tuple
mainframe.columnconfigure(0, weight=1) #resize as per window
mainframe.rowconfigure(0, weight=1) #resize as per window

#define feet and meters variables as StringVar() class
feet = StringVar()
meters = StringVar()

#this creates and places the feet_entry text box widget, giving
#it a width and the variable 'feet'
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

#
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)


#for each child of the mainframe widget, add padding
#this method can be used for other things as well
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()

#bind the return key to the calculate function
root.bind('<Return>', calculate)

#start the main loop
root.mainloop()
