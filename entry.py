#7. Entry() – User Input Field
#Description: Creates a text input field where the user can type.

from tkinter import *

root = Tk()

entry = Entry(root,show="*") #show=* ,hides typed characters like a password field.
entry.pack()

root.mainloop()