from tkinter import *
from tkinter import ttk, StringVar
from tkinter import messagebox
import sqlite3


class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1120x485+215+135")
        self.root.title("New Admin Registration")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.emp_id = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.contact_no = StringVar()
        self.password = StringVar()
        self.dob = StringVar()
        self.doj = StringVar()
        self.user_type = StringVar()
        self.salary = StringVar()

        main_frame = Frame(self.root, bg='lightyellow')
        main_frame.place(x=10, y=5, height=570, width=1100)

        main_label = Label(main_frame, text="New Admin Registration", font=("Goudy Old Style", 15, "bold"), bg="#0f4d7d",
                           fg="white")
        main_label.place(x=0, y=0, relwidth=1, height=35)

        emp_no_label = Label(main_frame, text="Emp No.:", font=("Goudy Old Style", 15), bg='lightyellow')
        emp_no_label.place(x=10, y=45)
        emp_no_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, textvariable=self.emp_id)
        emp_no_entry.place(x=120, y=45, width=150)

        name_label = Label(main_frame, text="Name", font=("Goudy Old Style", 15), bg='lightyellow')
        name_label.place(x=10, y=110)
        name_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, textvariable=self.name)
        name_entry.place(x=120, y=110, width=150)

        email_label = Label(main_frame, text="Email", font=("Goudy Old Style", 15), bg='lightyellow')
        email_label.place(x=10, y=175)
        email_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, textvariable=self.email)
        email_entry.place(x=120, y=175, width=150)

        gender_label = Label(main_frame, text="Gender", font=("Goudy Old Style", 15), bg='lightyellow')
        gender_label.place(x=310, y=45)
        gender_entry = ttk.Combobox(main_frame, font=("Goudy Old Style", 15), justify=CENTER,
                                    values=('Select', 'Male', 'Female', 'Other'), state="readonly",
                                    textvariable=self.gender)
        gender_entry.current(0)
        gender_entry.place(x=420, y=45, width=150)

        dob_label = Label(main_frame, text="DOB", font=("Goudy Old Style", 15), bg='lightyellow')
        dob_label.place(x=310, y=110)
        dob_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, textvariable=self.dob)
        dob_entry.place(x=420, y=110, width=150)

        password_label = Label(main_frame, text="Password", font=("Goudy Old Style", 15), bg='lightyellow')
        password_label.place(x=310, y=175)
        password_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2,
                               textvariable=self.password)
        password_entry.place(x=420, y=175, width=150)

        contact_label = Label(main_frame, text="Contact", font=("Goudy Old Style", 15), bg='lightyellow')
        contact_label.place(x=610, y=45)
        contact_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2,
                              textvariable=self.contact_no)
        contact_entry.place(x=720, y=45, width=150)

        doj_label = Label(main_frame, text="DOJ", font=("Goudy Old Style", 15), bg='lightyellow')
        doj_label.place(x=610, y=110)
        doj_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, textvariable=self.doj)
        doj_entry.place(x=720, y=110, width=150)

        user_type_label = Label(main_frame, text="User Type", font=("Goudy Old Style", 15), bg='lightyellow')
        user_type_label.place(x=610, y=175)
        user_type_entry = ttk.Combobox(main_frame, font=("Goudy Old Style", 15), justify=CENTER,
                                       values=('Admin'), state="readonly",
                                       textvariable=self.user_type)
        user_type_entry.current(0)
        user_type_entry.place(x=720, y=175, width=150)

        address_label = Label(main_frame, text="Address", font=("Goudy Old Style", 15), bg='lightyellow')
        address_label.place(x=10, y=240)
        self.address_entry = Text(main_frame, font=("Goudy Old Style", 13), bd=2, width=48,
                                  height=6)
        self.address_entry.place(x=120, y=240)

        salary_label = Label(main_frame, text="Salary", font=("Goudy Old Style", 15), bg='lightyellow')
        salary_label.place(x=610, y=240)
        salary_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, textvariable=self.salary)
        salary_entry.place(x=720, y=240, width=150)

        save_btn = Button(main_frame, text="Save", font=("Goudy Old Style", 15), bg="#33bbf9", cursor="hand2",
                          command=self.add)
        save_btn.place(x=300, y=400, width=150, height=35)

        clear_btn = Button(main_frame, text="Clear", font=("Goudy Old Style", 15), bg="#607d8b", cursor="hand2",
                           command=self.clear)
        clear_btn.place(x=500, y=400, width=150, height=35)

    def add(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()

        if self.emp_id.get() == "":
            messagebox.showerror('Error!', "Employee ID Is Mandatory", parent=self.root)
        else:
            cur.execute("SELECT * FROM employees WHERE eid=?", (self.emp_id.get(),))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror('Error!', 'Employee ID already assigned, try with a different ID',
                                     parent=self.root)
            else:
                cur.execute(
                    "INSERT INTO employees (eid, name, Email, gender, Contact, dob, doj, password, user_type, address, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        self.emp_id.get(),
                        self.name.get(),
                        self.email.get(),
                        self.gender.get(),
                        self.contact_no.get(),
                        self.dob.get(),
                        self.doj.get(),
                        self.password.get(),
                        self.user_type.get(),
                        self.address_entry.get('1.0', END),
                        self.salary.get(),

                    ))
            con.commit()
            messagebox.showinfo('Success!', 'record saved successfully!', parent=self.root)

    def clear(self):
        self.emp_id.set("")
        self.name.set("")
        self.email.set("")
        self.gender.set("Select")
        self.contact_no.set("")
        self.dob.set("")
        self.doj.set("")
        self.password.set("")
        self.user_type.set("Select")
        self.address_entry.delete('1.0', END)
        self.salary.set("")


if __name__ == '__main__':
    root4 = Tk()
    obj = Register(root4)
    root4.mainloop()
