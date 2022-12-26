from tkinter import *
from tkinter import messagebox
import os

root = Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
font = "Bahnschrift"
bg_color = "#90CCF4"
fg_color = "#19181A"

class SM:
    def __init__(self, root):
        self.root = root
        self.root.geometry("%dx%d+0+0" % (width, height))
        self.root.title("Store Manager")
        # self.root.attributes('-fullscreen', True)

        #--title--
        title = Label(self.root, text="Store Manager",
                      font=(font, 35, "bold"), fg=fg_color, bg=bg_color,
                      anchor = "w", padx = 20, pady = 20).place(x = 0, y = 0, relwidth=1, height= 70)

        #--logout--
        btn_logout = Button(self.root, text="Logout", font=(font, 15), bg = "#000080", bd = 4,
                            fg = "white", cursor="hand2").place(x= 1110, y = 15, height = 40, width = 150)

        self.clock_lbl = Label(self.root, text="Welcome to Store Manager ! \t\t\t\t\t\t\t\t  Datetime: DD-MM-YYYY  HH:MM:SS",
                               anchor="w", font=(font, 15), fg=fg_color, bg="#b0e0e6", padx= 20)
        self.clock_lbl.place(x = 0, y = 70, relwidth=1, height= 30)

        leftNav = Frame(self.root, bd = 2, relief=RIDGE, padx=5, pady=10)
        leftNav.place(x = 2, y = 102, width = 220, height = 535)

        # lbl_menu = Label(leftNav, text="Inventory", font=(font, 18), bg = "#40e0d0", padx=5, pady=5).pack(side=TOP, fill=X)
        btn_product = Button(leftNav, text="Products", font=(font, 18), bg="#008080", bd=4, fg="white", cursor="hand2").pack(side=TOP, fill=X, pady=8, padx=5)
        btn_supplier = Button(leftNav, text="Supplier", font=(font, 18), bg="#008080", bd=4, fg="white", cursor="hand2").pack(side=TOP, fill=X, pady=8, padx=5)
        btn_invoice = Button(leftNav, text="Invoice", font=(font, 18), bg="#008080", bd=4, fg="white", cursor="hand2").pack(side=TOP, fill=X, pady=8, padx=5)
        btn_analysis = Button(leftNav, text="Analysis", font=(font, 18), bg="#008080", bd=4, fg="white", cursor="hand2").pack(side=TOP, fill=X, pady=8, padx=5)
        btn_employee = Button(leftNav, text="Employee", font=(font, 18), bg="#008080", bd=4, fg="white", cursor="hand2").pack(side=TOP, fill=X, pady=8, padx=5)
        btn_customer = Button(leftNav, text="Customer", font=(font, 18), bg="#008080", bd=4, fg="white", cursor="hand2").pack(side=TOP, fill=X, pady=8, padx=5)

shop = SM(root)

def Exit():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()

root.protocol("WM_DELETE_WINDOW", Exit)
root.mainloop()
