#LEFT – Widget Position
#Description: Places widgets to the left side using pack.

from tkinter import *

root = Tk()

button1 = Button(root, text="Button 1")
button1.pack(side=LEFT)


root.mainloop()