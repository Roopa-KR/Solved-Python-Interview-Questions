#DISABLED – Disable Widget
#Description: Prevents user interaction with a widget.

from tkinter import *

root = Tk()

button = Button(root, text="Disabled Button", state=DISABLED)
button.pack()

root.mainloop()