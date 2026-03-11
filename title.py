#When we create the window using Tk(), we can add widgets to it, such as labels, buttons, and entry fields.
#the name of the window can be given using the title() method. 
# This method takes a string as an argument, which will be displayed as the title of the window.
#1. Tk() – Create Main Window
#Description: Creates the main window of the Tkinter application.

import tkinter as tk

root = tk.Tk()   # Creating main window
root.title("My Tkinter App")  # Setting the title of the window
root.mainloop()
