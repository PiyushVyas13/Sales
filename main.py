from tkinter import *
from PIL import Image, ImageTk
from employee import Employee
from supplier import Supplier
from category import Category
from product import Product
import sqlite3
import sys
import os
from tkinter import messagebox
from sale import Sale
import time


class Sales:
    def __init__(self, root):
        self.root2 = root
        self.root2.geometry("1350x690+0+0")
        self.root2.title("Company Name Billing")
        self.root2.config(bg="white")


        self.logo = PhotoImage(file="images/logo.png")
        title_label = Label(self.root2, text="V Mart", font=("Times New Roman", 40, "bold"), image=self.logo, compound=LEFT, bg="#010c48", fg="white", anchor='w', padx=20)
        title_label.place(x=0, y=0, relwidth=1, height=70)
        logout_btn = Button(self.root2, text="Logout", font=("Times New Roman", 15, "bold"), bg='yellow', cursor="hand2", command=self.logout)
        logout_btn.place(x=1100, y=15, height=40, width=150)

        self.clock_label = Label(self.root2, text="Admin Dashboard \t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS", font=("Times New Roman", 15), bg="#4d636d", fg="white", bd=3, relief=RIDGE)
        self.clock_label.place(x=0, y=70, relwidth=1, height=30)

        left_menu = Frame(self.root2, bd=2, relief=RIDGE)
        left_menu.place(x=0, y=100, width=200, height=515)
        self.left_menu_img = ImageTk.PhotoImage(file="images/bg1.jpg")
        image_label = Label(left_menu, image=self.left_menu_img)
        image_label.place(x=0, y=0, width=195, height=200)
        menu_label = Label(left_menu, text="Menu", font=("Times New Roman", 20, "bold"), bg="#009688", fg="white", padx=20)
        menu_label.place(x=0, y=200, relwidth=1)

        self.next_img = PhotoImage(file="images/next.png")
        employee_button = Button(left_menu, text="Employees", font=("Times New Roman", 20, "bold"), image=self.next_img, compound=LEFT, anchor='w', padx=5, command=self.employee)
        employee_button.place(x=0, y=240, relwidth=1, height=45)

        supplier_button = Button(left_menu, text="Suppliers", font=("Times New Roman", 20, "bold"), image=self.next_img, compound=LEFT, anchor='w', padx=5, command=self.supplier)
        supplier_button.place(x=0, y=285, relwidth=1, height=45)

        category_button = Button(left_menu, text="Categories", font=("Times New Roman", 20, "bold"), image=self.next_img, compound=LEFT, anchor='w', padx=5, command=self.category)
        category_button.place(x=0, y=330, relwidth=1, height=45)

        products_button = Button(left_menu, text="Products", font=("Times New Roman", 20, "bold"), image=self.next_img, compound=LEFT, anchor='w', padx=5, command=self.product)
        products_button.place(x=0, y=375, relwidth=1, height=45)

        sales_button = Button(left_menu, text="Sales", font=("Times New Roman", 20, "bold"), image=self.next_img, compound=LEFT, anchor='w', padx=5, command=self.sale)
        sales_button.place(x=0, y=420, relwidth=1, height=45)

        exit_button = Button(left_menu, text="Exit", font=("Times New Roman", 20, "bold"), image=self.next_img, compound=LEFT, anchor='w', padx=5, command=self.exit)
        exit_button.place(x=0, y=465, relwidth=1, height=45)

        self.employee_label = Label(self.root2, text=f"Total Employees \n [ 0 ]", bg="#33bbf9", bd=2, relief=RIDGE, font=("Goudy Old Style", 20, "bold"), fg="white")
        self.employee_label.place(x=330, y=120, width=300, height=150)

        self.supplier_label = Label(self.root2, text=f"Total Suppliers \n [ 0 ]", bg="#ff5722", bd=2, relief=RIDGE, font=("Goudy Old Style", 20, "bold"), fg="white")
        self.supplier_label.place(x=680, y=120, width=300, height=150)

        self.category_label = Label(self.root2, text=f"Total Categories \n [ 0 ]", bg="#009688", bd=2, relief=RIDGE, font=("Goudy Old Style", 20, "bold"), fg="white")
        self.category_label.place(x=1030, y=120, width=300, height=150)

        self.products_label = Label(self.root2, text="Total Products \n [ 0 ]", bg="#607d8b", bd=2, relief=RIDGE, font=("Goudy Old Style", 20, "bold"), fg="white")
        self.products_label.place(x=330, y=290, width=300, height=150)

        self.sales_label = Label(self.root2, text="Total Sales \n [ 0 ]", bg="#ffc107", bd=2, relief=RIDGE, font=("Goudy Old Style", 20, "bold"), fg="white")
        self.sales_label.place(x=680, y=290, width=300, height=150)


        footer_label = Label(self.root2, text="Company Name Private Limited Billing | Developer: Piyush Vyas \n For Any Technical Issue, Contact: +91 7028576670 \n" + u'\u00A9' + "Piyush Vyas. All Rights Reserved", font=("Times New Roman", 10), bg="#4d636d", bd=2, relief=RIDGE)
        footer_label.place(x=0, y=640, relwidth=1)

        self.time()
        self.get_records()

    def employee(self):
        self.new_win = Toplevel(self.root2)
        self.new_obj = Employee(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root2)
        self.new_obj = Supplier(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root2)
        self.new_obj = Category(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root2)
        self.new_obj = Product(self.new_win)

    def get_records(self):
        con = sqlite3.connect(database=r"employee_database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
        length = len(rows)
        self.employee_label.config(text=f"Total Employees \n [ {length} ]")

        cur.execute("SELECT * FROM suppliers")
        rows = cur.fetchall()
        length = len(rows)
        self.supplier_label.config(text=f"Total Suppliers \n [ {length} ]")

        cur.execute("SELECT * FROM categories")
        rows = cur.fetchall()
        length = len(rows)
        self.category_label.config(text=f"Total Categories \n [ {length} ]")

        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
        length = len(rows)
        self.products_label.config(text=f"Total Products \n [ {length} ]")

        d = os.listdir('bills')
        le = len(d)
        self.sales_label.config(text=f"Total Sales \n [ {le} ]")

        self.employee_label.after(200, self.get_records)

        con.commit()
        con.close()


    def exit(self):
        confirm = messagebox.askyesno('Confirm', 'Do You Really Want To Exit?')
        if confirm == True:
            sys.exit()

    def sale(self):
        self.new_win = Toplevel(self.root2)
        self.new_obj = Sale(self.new_win)

    def time(self):
        t = time.strftime("%I:%M:%S %p")
        d = time.strftime("%d/%m/%Y")
        self.clock_label.config(text=f"Admin Dashboard \t\t Date: {d} \t\t Time: {t}")
        self.clock_label.after(200, self.time)

    def logout(self):
        confirm = messagebox.askyesno('Confirm', 'Do You Really Want To Logout?', parent=self.root2)
        if confirm == True:
            self.root2.destroy()

if __name__ == '__main__':
    root = Tk()
    obj = Sales(root)
    root.mainloop()