# get() – Retrieve Entry Value
#Description: Retrieves text entered in an Entry widget.

from tkinter import *

root = Tk()

entry = Entry(root)
entry.pack()

def show():
    Label(root,text=entry.get()).pack()

button = Button(root, text="Show Input", command=show)
button.pack()

root.mainloop()
