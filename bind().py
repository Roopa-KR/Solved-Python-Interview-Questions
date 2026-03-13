 #bind() – Event Handling
#Description: Connects events (mouse, keyboard) to functions.

import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Click the button")
label.pack()

def clicked(event):
    label.config(text="Button clicked")

button = tk.Button(root, text="Click")
button.pack()

button.bind("<Button-1>", clicked)

root.mainloop()
