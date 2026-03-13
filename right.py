#Right – Widget Position
#Description: Places widgets to the right side using pack.

from tkinter import *

root = Tk()

button2 = Button(root, text="Button 2")
button2.pack(side=RIGHT)

root.mainloop()