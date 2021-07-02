from tkinter import *
from tkinter import ttk, StringVar
from tkinter import messagebox
import sqlite3


class Supplier:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1120x485+215+135")
        self.root.title("Supplier Details/New Supplier Registration")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.invoice_no = StringVar()
        self.name = StringVar()
        self.contact = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        select_by = ttk.Combobox(self.root, state="readonly", justify=CENTER, font=("Goudy Old Style", 15), textvariable=self.search_by)
        select_by.place(x=680, y=57, width=130)
        select_by['values'] = ['Select', 'invoice', 'Name', 'Contact']
        select_by.current(0)

        search_text = Entry(self.root, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.search_txt)
        search_text.place(x=820, y=57, width=150)

        search_btn = Button(self.root, text="Search", font=("Goudy Old Style", 15), cursor="hand2", bg="#4caf50", fg="white", command=self.search)
        search_btn.place(x=980, y=55, width=130, height=30)

        main_frame = Frame(self.root)
        main_frame.place(x=10, y=15, height=570, width=660)

        main_label = Label(self.root, text="Supplier Details", font=("Goudy Old Style", 30, "bold"), bg="#0f4d7d", fg="white")
        main_label.place(x=0, y=0, relwidth=1, height=40)

        invoice_no_label = Label(main_frame, text="Invoice No.:", font=("Goudy Old Style", 15))
        invoice_no_label.place(x=10, y=45)
        invoice_no_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.invoice_no)
        invoice_no_entry.place(x=170, y=45, width=190)

        name_label = Label(main_frame, text="Supplier Name", font=("Goudy Old Style", 15))
        name_label.place(x=10, y=90)
        name_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.name)
        name_entry.place(x=170, y=90, width=190)

        contact_label = Label(main_frame, text="Contact No.", font=("Goudy Old Style", 15))
        contact_label.place(x=10, y=135)
        contact_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.contact)
        contact_entry.place(x=170, y=135, width=190)

        desc_label = Label(main_frame, text="Description", font=("Goudy Old Style", 15))
        desc_label.place(x=10, y=180)
        self.desc_entry = Text(main_frame, font=("Goudy Old Style", 13), bd=2, bg="lightyellow", width=48,
                                  height=7)
        self.desc_entry.place(x=170, y=180)

        save_btn = Button(main_frame, text="Save", font=("Goudy Old Style", 15), bg="#33bbf9", cursor="hand2",
                          command=self.add)
        save_btn.place(x=10, y=365, width=100, height=30)

        update_btn = Button(main_frame, text="Update", font=("Goudy Old Style", 15), bg="#009688", cursor="hand2",
                            command=self.update)
        update_btn.place(x=120, y=365, width=100, height=30)

        delete_btn = Button(main_frame, text="Delete", font=("Goudy Old Style", 15), bg="#ff5722", cursor="hand2",
                            command=self.delete)
        delete_btn.place(x=230, y=365, width=100, height=30)

        clear_btn = Button(main_frame, text="Clear", font=("Goudy Old Style", 15), bg="#607d8b", cursor="hand2",
                           command=self.clear)
        clear_btn.place(x=340, y=365, width=100, height=30)

        info_frame = Frame(self.root, bd=2, relief=RIDGE)
        info_frame.place(x=680, y=92, width=430, height=385)

        scrolly = Scrollbar(info_frame, orient=VERTICAL)
        scrollx = Scrollbar(info_frame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.supplier_table = ttk.Treeview(info_frame, columns=("invoice", "name", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.supplier_table.heading("invoice", text="Invoice No.")
        self.supplier_table.heading("name", text="Name")
        self.supplier_table.heading("contact", text="Contact No.")
        self.supplier_table.heading("desc", text="Description")

        self.supplier_table['show'] = "headings"

        self.supplier_table.column("invoice", width=90)
        self.supplier_table.column("name", width=100)
        self.supplier_table.column("contact", width=100)
        self.supplier_table.column("desc", width=100)

        scrollx.config(command=self.supplier_table.xview)
        scrolly.config(command=self.supplier_table.yview)

        self.supplier_table.pack(fill=BOTH, expand=1)
        self.supplier_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def add(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()

        if self.invoice_no.get() == "":
            messagebox.showerror('Error!', "Invoice No. Is Mandatory", parent=self.root)
        else:
            cur.execute("SELECT * FROM suppliers WHERE invoice=?", (self.invoice_no.get(),))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror('Error!', 'Invoice No. already assigned, try with a different ID', parent=self.root)
            else:
                cur.execute(
                    "INSERT INTO suppliers (invoice, Name, Contact, desc) VALUES (?, ?, ?, ?)",
                    (
                        self.invoice_no.get(),
                        self.name.get(),
                        self.contact.get(),
                        self.desc_entry.get('1.0', END),
                    ))
                messagebox.showinfo('Success!', 'supplier added successfully!', parent=self.root)
            con.commit()
            self.show()

    def show(self):
        con = sqlite3.connect(database=r"employee_database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM suppliers")
        rows = cur.fetchall()
        self.supplier_table.delete(*self.supplier_table.get_children())
        for row in rows:
            self.supplier_table.insert('', END, values=row)

    def get_data(self, ev):
        f = self.supplier_table.focus()
        content = (self.supplier_table.item(f))
        row = content['values']
        self.invoice_no.set(row[0]),
        self.name.set(row[1]),
        self.contact.set(row[2]),
        self.desc_entry.delete('1.0', END),
        self.desc_entry.insert(END, row[3]),

    def update(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()
        if self.invoice_no.get() == "":
            messagebox.showerror('Error!', "Invoice No. Is Mandatory", parent=self.root)
        else:
            cur.execute("SELECT * FROM suppliers WHERE invoice=?", (self.invoice_no.get(),))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror('Error!', 'Invalid Invoice No.', parent=self.root)
            else:
                cur.execute(
                    "UPDATE suppliers SET Name=?, Contact=?, desc=? WHERE invoice=?",
                    (
                        self.name.get(),
                        self.contact.get(),
                        self.desc_entry.get('1.0', END),
                        self.invoice_no.get(),

                    ))
                con.commit()
                messagebox.showinfo('Success!', 'supplier updated successfully!', parent=self.root)
                self.show()

    def delete(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()

        cur.execute("SELECT * FROM suppliers WHERE invoice=?", (self.invoice_no.get(),))
        if self.invoice_no.get() == "":
            messagebox.showerror('Error!', 'Invoice No. Is Mandatory', parent=self.root)
        else:
            confirm = messagebox.askyesno('Confirm', 'Do You Really Want To Delete This Record?', parent=self.root)
            if confirm == True:
                cur.execute("DELETE FROM suppliers WHERE invoice=?", (self.invoice_no.get(),))
                messagebox.showinfo('Success', 'Record Deleted Successfully', parent=self.root)
        con.commit()
        self.show()
        self.clear()

    def clear(self):
        self.invoice_no.set("")
        self.name.set("")
        self.contact.set("")
        self.desc_entry.delete('1.0', END)
        self.search_by.set("Select")
        self.search_txt.set("")

    def search(self):
        con = sqlite3.connect(database=r"employee_database.db")
        cur = con.cursor()

        if self.search_by.get() == "Select":
            messagebox.showerror('Error!', 'Select a search option', parent=self.root)
        elif self.search_txt.get() == "":
            messagebox.showerror('Error!', 'Please provide a search input', parent=self.root)
        else:
            cur.execute(
                "SELECT * FROM suppliers WHERE " + self.search_by.get() + " LIKE '%" + self.search_txt.get() + "%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.supplier_table.delete(*self.supplier_table.get_children())
                for row in rows:
                    self.supplier_table.insert('', END, values=row)
            else:
                messagebox.showerror('Error!', 'No Record Found', parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = Supplier(root)
    root.mainloop()