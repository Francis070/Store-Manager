from tkinter import *
import os

root = Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

class SM:
    def __init__(self, root):
        self.root = root
        self.root.geometry("%dx%d+0+0" % (width, height))
        self.root.title("Store Manager")
        # self.root.attributes('-fullscreen', True)
        




shop = SM(root)

root.mainloop()
