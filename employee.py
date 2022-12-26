from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
font = "Bahnschrift"
bg_color = "#90CCF4"
fg_color = "#19181A"

class employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1050x500+220+130")
        self.root.title("Employee")
        self.root.focus_force()

        #Search Box
        searchFrame = LabelFrame(self.root, text="Search Employee", font = (font, 18, "bold"),
                                 bd = 3, relief= RIDGE)
        searchFrame.place(x = 250, y = 20, width=600, height=80)


        cmb_search = ttk.Combobox(searchFrame, state='readonly', justify=CENTER, font=(font, 14), values=("Select", "Name", "ID", "Contact No.", "Email"))
        cmb_search.place(x = 10, y = 10, width=180)
        cmb_search.current(0)

        search_text = Entry(searchFrame, font=(font, 14), bg="lightyellow").place(x = 200, y = 10, height=30)
        search_btn = Button(searchFrame, text="Search", font=(font, 15), bg="#7fffd4",
                            cursor="hand2").place(x = 415, y = 9, width=150, height=30)

        #--title
        emp_title = Label(self.root, text= "Employee Details", font = (font, 18, "bold"),
                          bg = "#2F4F4F", fg = "white").place(x = 30, y = 120, width=1000)

if __name__ == '__main__':
    root = Tk()
    shop = employee(root)
    root.mainloop()