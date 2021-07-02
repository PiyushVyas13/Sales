from tkinter import *
from tkinter import ttk, StringVar
from tkinter import messagebox
import sqlite3
import random


class Product:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1120x485+215+135")
        self.root.title("Add Products")
        self.root.config(bg="lightyellow")
        self.root.focus_force()

        self.pid = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.category = StringVar()
        self.supplier = StringVar()
        self.name = StringVar()
        self.price = StringVar()
        self.qty = StringVar()
        self.status = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        self.get_cat_sup()

        main_frame = Frame(self.root, bd=3, relief=RIDGE)
        main_frame.place(x=5, y=5, height=470, width=450)

        main_label = Label(main_frame, text="Manage Product Details", font=("Goudy Old Style", 20, "bold"), bg="#0f4d7d", fg="white")
        main_label.place(x=0, y=0, relwidth=1, height=35)

        pid_label = Label(main_frame, text="Prod ID.", font=("Goudy Old Style", 15))
        pid_label.place(x=15, y=55)
        pid_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.pid, state="readonly")
        pid_entry.place(x=135, y=55, width=150)

        category_label = Label(main_frame, text="Category", font=("Goudy Old Style", 15))
        category_label.place(x=15, y=105)
        category_entry = ttk.Combobox(main_frame, font=("Goudy Old Style", 15), justify=CENTER, values=self.cat_list, state="readonly", textvariable=self.category)
        category_entry.current(0)
        category_entry.place(x=135, y=105, width=150)

        supplier_label = Label(main_frame, text="Supplier", font=("Goudy Old Style", 15))
        supplier_label.place(x=15, y=155)
        supplier_entry = ttk.Combobox(main_frame, font=("Goudy Old Style", 15), justify=CENTER, values=self.sup_list, state="readonly", textvariable=self.supplier)
        supplier_entry.current(0)
        supplier_entry.place(x=135, y=155, width=150)

        name_label = Label(main_frame, text="Name", font=("Goudy Old Style", 15))
        name_label.place(x=15, y=205)
        name_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.name)
        name_entry.place(x=135, y=205, width=150)

        price_label = Label(main_frame, text="Price", font=("Goudy Old Style", 15))
        price_label.place(x=15, y=255)
        price_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.price)
        price_entry.place(x=135, y=255, width=150)

        qty_label = Label(main_frame, text="QTY", font=("Goudy Old Style", 15))
        qty_label.place(x=15, y=305)
        qty_entry = Entry(main_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.qty)
        qty_entry.place(x=135, y=305, width=150)

        status_label = Label(main_frame, text="Status", font=("Goudy Old Style", 15))
        status_label.place(x=15, y=355)
        status_entry = ttk.Combobox(main_frame, font=("Goudy Old Style", 15), justify=CENTER, values=('Active', 'Inactive'), state="readonly", textvariable=self.status)
        status_entry.current(0)
        status_entry.place(x=135, y=355, width=150)

        add_btn = Button(main_frame, text="Add", font=("Goudy Old Style", 15), bg="#33bbf9", cursor="hand2", command=self.add)
        add_btn.place(x=5, y=415, width=100, height=30)

        update_btn = Button(main_frame, text="Update", font=("Goudy Old Style", 15), bg="#009688", cursor="hand2", command=self.update)
        update_btn.place(x=115, y=415, width=100, height=30)

        delete_btn = Button(main_frame, text="Delete", font=("Goudy Old Style", 15), bg="#ff5722", cursor="hand2", command=self.delete)
        delete_btn.place(x=225, y=415, width=100, height=30)

        clear_btn = Button(main_frame, text="Clear", font=("Goudy Old Style", 15), bg="#607d8b", cursor="hand2", command=self.clear)
        clear_btn.place(x=335, y=415, width=100, height=30)

        search_frame = LabelFrame(self.root, text="Search Products", font=("Times New Roman", 12), bd=2, relief=RIDGE, bg="white")
        search_frame.place(x=465, y=10, width=640, height=80)

        select_by = ttk.Combobox(search_frame, state="readonly", justify=CENTER, font=("Goudy Old Style", 15), textvariable=self.search_by)
        select_by.place(x=10, y=10, width=180)
        select_by['values'] = ['Select', 'category', 'supplier', 'name', 'status']
        select_by.current(0)

        search_text = Entry(search_frame, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.search_txt)
        search_text.place(x=200, y=10, width=250)

        search_btn = Button(search_frame, text="Search", font=("Goudy Old Style", 15), cursor="hand2", bg="#4caf50", fg="white", command=self.search)
        search_btn.place(x=470, y=10, width=150, height=30)

        info_frame = Frame(self.root, bd=2, relief=RIDGE)
        info_frame.place(x=465, y=100, width=640, height=375)

        scrolly = Scrollbar(info_frame, orient=VERTICAL)
        scrollx = Scrollbar(info_frame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.product_table = ttk.Treeview(info_frame, columns=("pid", "category", "supplier", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.product_table.heading("pid", text="Prod ID.")
        self.product_table.heading("category", text="Category")
        self.product_table.heading("supplier", text="Supplier")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Quantity")
        self.product_table.heading("status", text="Status")

        self.product_table['show'] = "headings"

        self.product_table.column("pid", width=90)
        self.product_table.column("category", width=100)
        self.product_table.column("supplier", width=100)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=100)
        self.product_table.column("qty", width=100)
        self.product_table.column("status", width=100)

        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def get_cat_sup(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()

        cur.execute("SELECT name FROM categories")
        rows = cur.fetchall()
        self.cat_list.append("Select")
        for row in rows:
            self.cat_list.append(row[0])

        cur.execute("SELECT Name FROM suppliers")
        rows = cur.fetchall()
        self.sup_list.append("Select")
        for row in rows:
            self.sup_list.append(row[0])

    def add(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()

        if (self.category.get() == "Select" and self.supplier.get() == "Select") or (self.category.get() == "Select") or (self.supplier.get() == "Select"):
            messagebox.showerror('Error!', "Category And Supplier Name Are Mandatory", parent=self.root)
        else:
            cur.execute("SELECT * FROM products WHERE pid=?", (self.pid.get(),))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror('Error!', 'Product ID already assigned, try with a different ID',
                                     parent=self.root)
            else:
                cur.execute(
                    "INSERT INTO products (category, supplier, name, price, qty, status) VALUES (?, ?, ?, ?, ?, ?)",
                    (
                        self.category.get(),
                        self.supplier.get(),
                        self.name.get(),
                        self.price.get(),
                        self.qty.get(),
                        self.status.get(),
                    ))
            con.commit()
            messagebox.showinfo('Success!', 'product added successfully!', parent=self.root)
            self.show()

    def show(self):
        con = sqlite3.connect(database=r"employee_database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
        self.product_table.delete(*self.product_table.get_children())
        for row in rows:
            self.product_table.insert('', END, values=row)

    def get_data(self, ev):
        f = self.product_table.focus()
        content = (self.product_table.item(f))
        row = content['values']
        self.pid.set(row[0])
        self.category.set(row[1]),
        self.supplier.set(row[2]),
        self.name.set(row[3]),
        self.price.set(row[4]),
        self.qty.set(row[5]),
        self.status.set(row[6]),

    def update(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()
        if self.pid.get() == "":
            messagebox.showerror('Error!', "Product ID Is Mandatory", parent=self.root)
        else:
            cur.execute("SELECT * FROM products WHERE pid=?", (self.pid.get(),))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror('Error!', 'Invalid Product ID', parent=self.root)
            else:
                cur.execute("UPDATE products SET category=?, supplier=?, name=?, price=?, qty=?, status=? WHERE pid=?", (
                        self.category.get(),
                        self.supplier.get(),
                        self.name.get(),
                        self.price.get(),
                        self.qty.get(),
                        self.status.get(),
                        self.pid.get(),

                ))
                messagebox.showinfo('Success!', 'record updated successfully!', parent=self.root)
                con.commit()
                self.show()

    def delete(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()

        cur.execute("SELECT * FROM products WHERE pid=?", (self.pid.get(),))
        if self.pid.get() == "":
            messagebox.showerror('Error!', 'Product ID Is Mandatory', parent=self.root)
        else:
            confirm = messagebox.askyesno('Confirm', 'Do You Really Want To Delete This Record?', parent=self.root)
            if confirm == True:
                cur.execute("DELETE FROM products WHERE pid=?", (self.pid.get(),))
                messagebox.showinfo('Success', 'Record Deleted Successfully', parent=self.root)
        con.commit()
        self.show()
        self.clear()

    def clear(self):
        self.pid.set("")
        self.name.set("")
        self.category.set("Select")
        self.supplier.set("Select")
        self.price.set("")
        self.qty.set("")
        self.status.set("Active")
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
            cur.execute("SELECT * FROM products WHERE " + self.search_by.get() + " LIKE '%" + self.search_txt.get() + "%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.product_table.delete(*self.product_table.get_children())
                for row in rows:
                    self.product_table.insert('', END, values=row)
            else:
                messagebox.showerror('Error!', 'No Record Found', parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = Product(root)
    root.mainloop()