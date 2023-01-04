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
        self.address = StringVar()
        self.salary = StringVar()

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

        ## ------ ROW 1 -----------
        lbl_empid = Label(self.root, text="Emp ID.", font=(font, 13), bg="white").place(x=250, y=270)
        txt_empid = Entry(self.root, textvariable=self.emp_id ,font=(font, 13), bg="lightyellow").place(x=320, y=270)

        lbl_gen = Label(self.root, text="Gender", font=(font, 13), bg="white").place(x=535, y=270)
        # gen_txt = Entry(self.root, textvariable=self.gender ,font=(font, 13), bg="lightyellow").place(x=600, y=270)
        cmb_gen = ttk.Combobox(self.root, state='readonly', textvariable=self.gender, justify=CENTER,
                                  font=(font, 13), values=("Select", "Male", "Female", "Other"))
        cmb_gen.place(x=600, y=270, width=180)
        cmb_gen.current(0)

        lbl_contact = Label(self.root, text="Contact", font=(font, 13), bg="white").place(x=815, y=270)
        txt_contact = Entry(self.root, textvariable=self.contact ,font=(font, 13), bg="lightyellow").place(x=885, y=270)

        ## -------- ROW 2 ------------

        lbl_name = Label(self.root, text="Name", font=(font, 13), bg="white").place(x=250, y=320)
        txt_name = Entry(self.root, textvariable=self.name, font=(font, 13), bg="lightyellow").place(x=320, y=320)

        lbl_email = Label(self.root, text="Email", font=(font, 13), bg="white").place(x=535, y=320)
        txt_email = Entry(self.root, textvariable=self.email, font=(font, 13), bg="lightyellow").place(x=600, y=320)

        lbl_dob = Label(self.root, text="D.O.B", font=(font, 13), bg="white").place(x=815, y=320)
        txt_dob = Entry(self.root, textvariable=self.dob, font=(font, 13), bg="lightyellow").place(x=885, y=320)

        ##-------- ROW 3 -------------

        lbl_doj = Label(self.root, text="D.O.J", font=(font, 13), bg="white").place(x=250, y=370)
        txt_doj = Entry(self.root, textvariable=self.doj, font=(font, 13), bg="lightyellow").place(x=320, y=370)

        lbl_pwd = Label(self.root, text="Password", font=(font, 13), bg="white").place(x=535, y=370)
        txt_pwd = Entry(self.root, textvariable=self.password, font=(font, 13), bg="lightyellow").place(x=630, y=370)

        lbl_user = Label(self.root, text="User Type", font=(font, 13), bg="white").place(x=845, y=370)
        # txt_user = Entry(self.root, textvariable=self.user_type, font=(font, 13), bg="lightyellow").place(x=930, y=370)
        cmb_user = ttk.Combobox(self.root, state='readonly', textvariable=self.user_type, justify=CENTER,
                               font=(font, 13), values=("Select", "Admin", "Employee"))
        cmb_user.place(x=930, y=370, width=180)
        cmb_user.current(0)

        # ----- ROW 4 -------

        lbl_address = Label(self.root, text="Address", font=(font, 13), bg="white").place(x=250, y=420)
        self.txt_address = Text(self.root, font=(font, 13), bg="lightyellow")
        self.txt_address.place(x=320, y=420, width=300, height=60)


        lbl_salary = Label(self.root, text="Salary", font=(font, 13), bg="white").place(x=630, y=420)
        txt_salary = Entry(self.root, textvariable=self.salary, font=(font, 13), bg="lightyellow").place(x=700, y=420)

        ##buttons

        btn_save = Button(self.root, text = "Save",font=(font, 12), bg="#7fffd4",
                          cursor="hand2").place(x = 740, y = 460, width=70, height=25)
        btn_update = Button(self.root, text="Update", font=(font, 12), bg="#7fffd4",
                          cursor="hand2").place(x=810, y=460, width=70, height=25)
        btn_delete = Button(self.root, text="Delete", font=(font, 12), bg="#7fffd4",
                          cursor="hand2").place(x=880, y=460, width=70, height=25)
        btn_clear = Button(self.root, text="Clear", font=(font, 12), bg="#7fffd4",
                          cursor="hand2").place(x=950, y=460, width=70, height=25)

if __name__ == '__main__':
    root = Tk()
    shop = employee(root)
    root.mainloop()