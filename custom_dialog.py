#Custom Dialog

from tkinter import *

root = Tk()
root.geometry("400x500")
def open_login():
    dialog = Toplevel(root)

    Label(dialog, text="Username").pack()
    Entry(dialog).pack()

    Label(dialog, text="Password").pack()
    Entry(dialog, show="*").pack()

    Button(dialog, text="Login").pack()

Button(root, text="Open Login Dialog", command=open_login).pack()

root.mainloop()
