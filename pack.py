#pack() – Layout Manager
#Description: Places widgets in the window automatically.

from tkinter import *

root = Tk()

label1 = Label(root, text="First Label")
label1.pack()

label2 = Label(root, text="Second Label")
label2.pack()
root.mainloop()
#In this code, we import the tkinter library and create a root window. We then create two Label widgets with different text and use the pack() method to automatically place them in the window. Finally, we call mainloop() to run the application and keep the window open.