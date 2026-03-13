#Frame() – Container Widget
#Description: Used to group widgets together.

from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

Label(frame, text="Inside Frame").pack()

root.mainloop()

#example
from tkinter import *

root = Tk()

frame = Frame(root, bg="lightblue")
frame.pack(pady=20)

Label(frame, text="Username").pack()
username = Entry(frame)
username.pack()

Label(frame, text="Password").pack()
password = Entry(frame, show="*")
password.pack()

message = Label(frame, text="")
message.pack()

def login():
    message.config(text="Login Successful")

Button(frame, text="Login", command=login).pack()

root.mainloop()
