from tkinter import *
from tkinter import ttk, StringVar
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import random


class Category:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1120x485+215+135")
        self.root.title("Supplier Details/New Supplier Registration")
        self.root.config(bg="lightyellow")
        self.root.focus_force()

        self.category = StringVar()
        self.cid = 0
        self.img1 = ImageTk.PhotoImage(file='images/img1.jpg')
        self.img2 = ImageTk.PhotoImage(file='images/img2.jpg')

        main_label = Label(self.root, text="Manage Product Category", font=("Goudy Old Style", 30, "bold"), bg="#0f4d7d", fg="white")
        main_label.place(x=0, y=0, relwidth=1, height=45)

        category_label = Label(self.root, text="Enter Category Name", font=("Goudy Old Style", 25, "bold"), bg="lightyellow", fg="black")
        category_label.place(x=20, y=60)

        category_entry = Entry(self.root, font=("Goudy Old Style", 15), bd=3, bg="white", textvariable=self.category)
        category_entry.place(x=23, y=130, width=300, height=30)

        add_btn = Button(self.root, text="ADD", font=("Goudy Old Style", 15, "bold"), bg="#4caf50", cursor="hand2", fg='white', command=self.add)
        add_btn.place(x=22, y=185, width=100, height=30)

        delete_btn = Button(self.root, text="DELETE", font=("Goudy Old Style", 15, "bold"), bg="#ff5722", cursor="hand2", command=self.delete, fg='white')
        delete_btn.place(x=132, y=185, width=100, height=30)

        clear_btn = Button(self.root, text="CLEAR", font=("Goudy Old Style", 15), bg="#607d8b", cursor="hand2", command=self.clear, fg='white')
        clear_btn.place(x=242, y=185, width=100, height=30)

        img1_label = Label(self.root, image=self.img1, bd=3, relief=RIDGE)
        img1_label.place(x=20, y=250)

        img2_label = Label(self.root, image=self.img2, bd=3, relief=RIDGE)
        img2_label.place(x=360, y=250, height=215)

        info_frame = Frame(self.root, bd=2, relief=RIDGE)
        info_frame.place(x=720, y=60, width=390, height=195)

        scrolly = Scrollbar(info_frame, orient=VERTICAL)
        scrollx = Scrollbar(info_frame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.category_table = ttk.Treeview(info_frame, columns=("cid", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.category_table.heading("cid", text="Cat ID")
        self.category_table.heading("name", text="Category Name")

        self.category_table['show'] = "headings"

        self.category_table.column("cid", width=20)
        self.category_table.column("name", width=80)

        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)

        self.category_table.pack(fill=BOTH, expand=1)
        self.category_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def add(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()

        if self.category.get() == "":
            messagebox.showerror('Error!', "Category Name Is Mandatory", parent=self.root)
        else:
            self.cid = random.randrange(101, 999)
            cur.execute("SELECT * FROM categories WHERE cid=?", (self.cid,))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror('Error!', 'Category ID already assigned, try with a different ID', parent=self.root)
            else:
                cur.execute(
                    "INSERT INTO categories (cid, name) VALUES (?, ?)",
                    (
                        self.cid,
                        self.category.get(),
                    ))
                messagebox.showinfo('Success!', 'category added successfully!', parent=self.root)
            con.commit()
            self.show()

    def show(self):
        con = sqlite3.connect(database=r"employee_database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM categories")
        rows = cur.fetchall()
        self.category_table.delete(*self.category_table.get_children())
        for row in rows:
            self.category_table.insert('', END, values=row)

    def get_data(self, ev):
        f = self.category_table.focus()
        content = (self.category_table.item(f))
        row = content['values']
        self.category.set(row[1]),

    def delete(self):
        con = sqlite3.connect(database=r"employee_database.db")

        cur = con.cursor()

        cur.execute("SELECT * FROM categories WHERE cid=?", (self.cid,))
        if self.category.get() == "":
            messagebox.showerror('Error!', 'Category Name Is Mandatory', parent=self.root)
        else:
            confirm = messagebox.askyesno('Confirm', 'Do You Really Want To Delete This Record?', parent=self.root)
            if confirm == True:
                cur.execute("DELETE FROM categories WHERE name=?", (self.category.get(),))
                messagebox.showinfo('Success', 'Record Deleted Successfully', parent=self.root)
        con.commit()
        self.show()
        self.clear()

    def clear(self):
        self.category.set("")

if __name__ == '__main__':
    root = Tk()
    obj = Category(root)
    root.mainloop()