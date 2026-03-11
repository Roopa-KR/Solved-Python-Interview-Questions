#3. geometry() – Set Window Size
#Description: Defines the size of the window.

import tkinter as tk

root = tk.Tk()
root.geometry("400x300+600+100")# width = 400 pixels, height = 300 pixels
#,200 → distance from left of screen, 100 → distance from top of screen

root.mainloop()