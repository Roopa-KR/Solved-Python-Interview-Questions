 #config() – Change Widget Properties
#Description: Modifies widget properties after creation.

from tkinter import *

root = Tk()

label = Label(root, text="Hello")
label.pack()

def change():
    label.config(text="Text Changed",bg="lightblue")

button = Button(root, text="Change Text", command=change)
button.pack()

root.mainloop()