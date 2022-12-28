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
        # self.root.geometry("1050x500+220+130")
        # self.root.title("Employee")
        # self.root.focus_force()

        # all variables
        self.search_by = StringVar()
        self.search_text = StringVar()
        self.emp_id = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.dob = StringVar()
        self.doj = StringVar()
        self.password = StringVar()
        self.user_type = StringVar()


        #Search Box
        searchFrame = LabelFrame(self.root, text="Search Employee", font = (font, 18, "bold"),
                                 bd = 3, relief= RIDGE)
        searchFrame.place(x = 250, y = 110, width=600, height=80)


        cmb_search = ttk.Combobox(searchFrame, state='readonly', textvariable=self.search_by, justify=CENTER, font=(font, 14), values=("Select", "Name", "ID", "Contact No.", "Email"))
        cmb_search.place(x = 10, y = 10, width=180)
        cmb_search.current(0)

        search_text = Entry(searchFrame, textvariable=self.search_text, font=(font, 14), bg="lightyellow").place(x = 200, y = 10, height=30)
        search_btn = Button(searchFrame, text="Search", font=(font, 15), bg="#7fffd4",
                            cursor="hand2").place(x = 415, y = 9, width=150, height=30)

        #--title
        emp_title = Label(self.root, text= "Employee Details", font = (font, 18, "bold"),
                          bg = "#2F4F4F", fg = "white").place(x = 250, y = 210, width=1000)
        #--content--
        empid = Label(self.root, text="Emp ID.", font=(font, 13), bg="white").place(x=250, y=270)
        empid_txt = Entry(self.root, textvariable=self.emp_id ,font=(font, 13), bg="lightyellow").place(x=320, y=270)
        gen = Label(self.root, text="Gender", font=(font, 13), bg="white").place(x=535, y=270)
        # gen_txt = Entry(self.root, textvariable=self.gender ,font=(font, 13), bg="lightyellow").place(x=600, y=270)
        cmb_gen = ttk.Combobox(self.root, state='readonly', textvariable=self.gender, justify=CENTER,
                                  font=(font, 13), values=("Select", "Male", "Female", "Other"))
        cmb_gen.place(x=600, y=270, width=180)
        cmb_gen.current(0)

        # phn_no = Label(self.root, text="Contact", font=(font, 13), bg="white").place(x=250, y=270)
        # phn_txt = Entry(self.root, font=(font, 13), bg="lightyellow").place(x=320, y=270)

if __name__ == '__main__':
    root = Tk()
    shop = employee(root)
    root.mainloop()