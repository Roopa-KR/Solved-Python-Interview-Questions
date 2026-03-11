#1. Tk() – Create Main Window
#Description: Creates the main window of the Tkinter application.

import tkinter as tk

root = tk.Tk()   # Creating main window
root.mainloop()
#this code creates a main window using the Tk() function from the tkinter library.
# The mainloop() function is called to start the event loop, which keeps the window open and responsive to user interactions.
#without the mainloop() function, the window would open and close immediately, as the program would finish 
# executing without waiting for user input.