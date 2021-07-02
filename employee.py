from tkinter import *
from tkinter import ttk, StringVar
from tkinter import messagebox
import sqlite3


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1120x485+215+135")
        self.root.title("Employee Details/New Employee Registration")
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
        self.search_by = StringVar()
        self.search_txt = StringVar()

        search_frame = LabelFrame(self.root, text="Search Employee", font=("Times New Roman", 12), bd=2, relief=RIDGE, bg="white")
        search_frame.place(x=200, y=20, width=620, height=80)
        select_by = ttk.Combobox(search_frame, state="readonly", justify=CENTER, font=("Goudy Old Style", 15), textvariable=self.search_by)
        select_by.place(x=10, y=10, width=180)
        select_by['values'] = ['Select', 'eid', 'Name', 'Email', 'Contact']
        select_by.current(0)

        search_text = Entry(search_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.search_txt)
        search_text.place(x=200, y=10, width=250)

        search_btn = Button(search_frame, text="Search", font=("Goudy Old Style", 15), cursor="hand2", bg="#4caf50", fg="white", command=self.search)
        search_btn.place(x=460, y=10, width=150, height=30)

        main_frame = Frame(self.root)
        main_frame.place(x=10, y=115, height=270, width=1100)

        main_label = Label(main_frame, text="Employee Details", font=("Goudy Old Style", 15, "bold"), bg="#0f4d7d", fg="white")
        main_label.place(x=0, y=0, relwidth=1, height=35)

        emp_no_label = Label(main_frame, text="Emp No.:", font=("Goudy Old Style", 15))
        emp_no_label.place(x=10, y=45)
        emp_no_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.emp_id)
        emp_no_entry.place(x=120, y=45, width=150)

        name_label = Label(main_frame, text="Name", font=("Goudy Old Style", 15))
        name_label.place(x=10, y=90)
        name_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.name)
        name_entry.place(x=120, y=90, width=150)

        email_label = Label(main_frame, text="Email", font=("Goudy Old Style", 15))
        email_label.place(x=10, y=135)
        email_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.email)
        email_entry.place(x=120, y=135, width=150)

        gender_label = Label(main_frame, text="Gender", font=("Goudy Old Style", 15))
        gender_label.place(x=310, y=45)
        gender_entry = ttk.Combobox(main_frame, font=("Goudy Old Style", 15), justify=CENTER, values=('Select', 'Male', 'Female', 'Other'), state="readonly", textvariable=self.gender)
        gender_entry.current(0)
        gender_entry.place(x=420, y=45, width=150)

        dob_label = Label(main_frame, text="DOB", font=("Goudy Old Style", 15))
        dob_label.place(x=310, y=90)
        dob_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.dob)
        dob_entry.place(x=420, y=90, width=150)

        password_label = Label(main_frame, text="Password", font=("Goudy Old Style", 15))
        password_label.place(x=310, y=135)
        password_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.password)
        password_entry.place(x=420, y=135, width=150)

        contact_label = Label(main_frame, text="Contact", font=("Goudy Old Style", 15))
        contact_label.place(x=610, y=45)
        contact_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.contact_no)
        contact_entry.place(x=720, y=45, width=150)


        doj_label = Label(main_frame, text="DOJ", font=("Goudy Old Style", 15))
        doj_label.place(x=610, y=90)
        doj_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.doj)
        doj_entry.place(x=720, y=90, width=150)

        user_type_label = Label(main_frame, text="User Type", font=("Goudy Old Style", 15))
        user_type_label.place(x=610, y=135)
        user_type_entry = ttk.Combobox(main_frame, font=("Goudy Old Style", 15), justify=CENTER, values=('Select', 'Admin', 'Employee'), state="readonly", textvariable=self.user_type)
        user_type_entry.current(0)
        user_type_entry.place(x=720, y=135, width=150)

        address_label = Label(main_frame, text="Address", font=("Goudy Old Style", 15))
        address_label.place(x=10, y=180)
        self.address_entry = Text(main_frame, font=("Goudy Old Style", 13), bd=2, bg="lightyellow", width=28, height=3.3)
        self.address_entry.place(x=120, y=180)

        salary_label = Label(main_frame, text="Salary", font=("Goudy Old Style", 15))
        salary_label.place(x=420, y=177)
        salary_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.salary)
        salary_entry.place(x=530, y=177, width=150)

        save_btn = Button(main_frame, text="Save", font=("Goudy Old Style", 15), bg="#33bbf9", cursor="hand2", command=self.add)
        save_btn.place(x=420, y=220, width=100, height=30)

        update_btn = Button(main_frame, text="Update", font=("Goudy Old Style", 15), bg="#009688", cursor="hand2", command=self.update)
        update_btn.place(x=530, y=220, width=100, height=30)

        delete_btn = Button(main_frame, text="Delete", font=("Goudy Old Style", 15), bg="#ff5722", cursor="hand2", command=self.delete)
        delete_btn.place(x=640, y=220, width=100, height=30)

        clear_btn = Button(main_frame, text="Clear", font=("Goudy Old Style", 15), bg="#607d8b", cursor="hand2", command=self.clear)
        clear_btn.place(x=750, y=220, width=100, height=30)

        info_frame = Frame(self.root, bd=2, relief=RIDGE)
        info_frame.place(x=10, y=395, width=1100, height=85)

        scrolly = Scrollbar(info_frame, orient=VERTICAL)
        scrollx = Scrollbar(info_frame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.employee_table = ttk.Treeview(info_frame, columns=("eid", "name", "email", "gender", "contact_no", "dob", "password", "address", "doj", "user_type", "salary"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.employee_table.heading("eid", text="Emp ID")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("email", text="Email ID")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("contact_no", text="Contact No.")
        self.employee_table.heading("dob", text="Date Of Birth")
        self.employee_table.heading("doj", text="Date Of Joining")
        self.employee_table.heading("password", text="Password")
        self.employee_table.heading("user_type", text="User Type")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("salary", text="Salary")

        self.employee_table['show'] = "headings"

        self.employee_table.column("eid", width=90)
        self.employee_table.column("name", width=100)
        self.employee_table.column("email", width=100)
        self.employee_table.column("gender", width=100)
        self.employee_table.column("contact_no", width=100)
        self.employee_table.column("dob", width=100)
        self.employee_table.column("doj", width=100)
        self.employee_table.column("password", width=100)
        self.employee_table.column("user_type", width=100)
        self.employee_table.column("address", width=100)
        self.employee_table.column("salary", width=100)

        scrollx.config(command=self.employee_table.xview)
        scrolly.config(command=self.employee_table.yview)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()


    def add(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()
        
        if self.emp_id.get() == "":
            messagebox.showerror('Error!', "Employee ID Is Mandatory", parent=self.root)
        else:
            cur.execute("SELECT * FROM employees WHERE eid=?", (self.emp_id.get(),))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror('Error!', 'Employee ID already assigned, try with a different ID', parent=self.root)
            else:
                cur.execute("INSERT INTO employees (eid, name, Email, gender, Contact, dob, doj, password, user_type, address, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
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
                self.show()



    def show(self):
        con = sqlite3.connect(database=r"employee_database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
        self.employee_table.delete(*self.employee_table.get_children())
        for row in rows:
            self.employee_table.insert('', END, values=row)



    def get_data(self, ev):
        f = self.employee_table.focus()
        content = (self.employee_table.item(f))
        row = content['values']
        self.emp_id.set(row[0]),
        self.name.set(row[1]),
        self.email.set(row[2]),
        self.gender.set(row[3]),
        self.contact_no.set(row[4]),
        self.dob.set(row[5]),
        self.doj.set(row[8]),
        self.password.set(row[6]),
        self.user_type.set(row[9]),
        self.address_entry.delete('1.0', END),
        self.address_entry.insert(END, row[7]),
        self.salary.set(row[10]),

    def update(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()
        if self.emp_id.get() == "":
            messagebox.showerror('Error!', "Employee ID Is Mandatory", parent=self.root)
        else:
            cur.execute("SELECT * FROM employees WHERE eid=?", (self.emp_id.get(),))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror('Error!', 'Invalid Employee ID', parent=self.root)
            else:
                cur.execute("UPDATE employees SET name=?, email=?, gender=?, Contact=?, dob=?, doj=?, password=?, user_type=?, address=?, salary=? WHERE eid=?", (
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
                        self.emp_id.get(),

                ))
                messagebox.showinfo('Success!', 'record updated successfully!', parent=self.root)
                con.commit()
                self.show()


    def delete(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()

        cur.execute("SELECT * FROM employees WHERE eid=?", (self.emp_id.get(),))
        if self.emp_id.get() == "":
            messagebox.showerror('Error!', 'Employee ID Is Mandatory', parent=self.root)
        else:
            confirm = messagebox.askyesno('Confirm', 'Do You Really Want To Delete This Record?', parent=self.root)
            if confirm == True:
                cur.execute("DELETE FROM employees WHERE eid=?", (self.emp_id.get(),))
                messagebox.showinfo('Success', 'Record Deleted Successfully', parent=self.root)
        con.commit()
        self.show()
        self.clear()

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
        self.search_by.set("Select")
        self.search_txt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r"employee_database.db")
        cur = con.cursor()

        if self.search_by.get() == "Select":
            messagebox.showerror('Error!', 'Select a search option', parent=self.root)
        elif self.search_txt.get() == "":
            messagebox.showerror('Error!', 'Please provide a search input', parent=self.root)
        else:
            cur.execute("SELECT * FROM employees WHERE " + self.search_by.get() + " LIKE '%" + self.search_txt.get() + "%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.employee_table.delete(*self.employee_table.get_children())
                for row in rows:
                    self.employee_table.insert('', END, values=row)
            else:
                messagebox.showerror('Error!', 'No Record Found', parent=self.root)
        
            


if __name__ == '__main__':
    root = Tk()
    obj = Employee(root)
    root.mainloop()