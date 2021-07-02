from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os
import tempfile
from calculator import Calculator
import time

class EmployeeModule:
    def __init__(self, root):
        self.root3 = root
        self.root3.geometry("1350x690+0+0")
        self.root3.title("Company Name Employee Module")
        self.root3.config(bg="lightyellow")

        self.product_name = StringVar()
        self.ppq = StringVar()
        self.qty = StringVar()
        self.list = []
        self.list2 = []
        self.chk_print = 0
        self.amount_list = []
        self.name = StringVar()
        self.contact = StringVar()
        self.search_txt = StringVar()

        self.logo = PhotoImage(file="images/logo.png")
        title_label = Label(self.root3, text="Company Name", font=("Times New Roman", 40, "bold"), image=self.logo, compound=LEFT, bg="#010c48", fg="white", anchor='w', padx=20)
        title_label.place(x=0, y=0, relwidth=1, height=70)
        logout_btn = Button(self.root3, text="Logout", font=("Times New Roman", 15, "bold"), bg='yellow', cursor="hand2", command=self.logout)
        logout_btn.place(x=1100, y=15, height=40, width=150)

        self.clock_label = Label(self.root3, text="Employee Dashboard \t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS", font=("Times New Roman", 15), bg="#4d636d", fg="white", bd=3, relief=RIDGE)
        self.clock_label.place(x=0, y=70, relwidth=1, height=30)

        # Product Frame ======================================================================
        product_frame = Frame(self.root3, bd=3, relief=RIDGE)
        product_frame.place(x=5, y=110, width=400, height=150)

        product_label = Label(product_frame, text="All Products", font=("Times New Roman", 20, "bold"), bg='black', fg='white', bd=3, relief=RIDGE)
        product_label.place(x=0, y=0, relwidth=1)

        search_product_label = Label(product_frame, text="Search Products | By Name", font=("Times New Roman", 15), bg='white', fg='green')
        search_product_label.place(x=0, y=65)

        pname_label = Label(product_frame, text="Product Name", font=("Times New Roman", 15), bg='white', fg='black')
        pname_label.place(x=0, y=105)
        pname_entry = Entry(product_frame, font=("Times New Roman", 15), bg='lightyellow', textvariable=self.search_txt)
        pname_entry.place(x=120, y=105, width=150)

        show_all_btn = Button(product_frame, text="Show All", font=("Times New Roman", 15), fg='white', bg="navyblue", cursor="hand2", command=self.show1)
        show_all_btn.place(x=285, y=65, width=100, height=30)

        search_btn = Button(product_frame, text="Search", font=("Times New Roman", 15), fg='white', bg="#33bbf9", cursor="hand2", command=self.search)
        search_btn.place(x=285, y=105, width=100, height=30)

        # Product List Frame =========================================================
        product_list_frame = Frame(self.root3, bd=3, relief=RIDGE)
        product_list_frame.place(x=5, y=265, width=400, height=420)

        scrolly = Scrollbar(product_list_frame, orient=VERTICAL)
        scrollx = Scrollbar(product_list_frame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.product_table = ttk.Treeview(product_list_frame, columns=("pid", "category", "supplier", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
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

        # Customer Frame ===============================================================
        customer_frame = Frame(self.root3, bd=3, relief=RIDGE)
        customer_frame.place(x=405, y=110, width=550, height=80)

        customer_label = Label(customer_frame, text="Customer Details", font=("Times New Roman", 15, "bold"), bg='lightgray', fg='black')
        customer_label.place(x=0, y=0, relwidth=1, height=27)

        name_label = Label(customer_frame, text="Name", font=("Times New Roman", 15), bg='white')
        name_label.place(x=0, y=37, width=60)
        name_entry = Entry(customer_frame, font=("Times New Roman", 15), relief=GROOVE, bd=2, textvariable=self.name)
        name_entry.place(x=65, y=37, width=200)

        contact_label = Label(customer_frame, text="Contact", font=("Times New Roman", 15), bg='white')
        contact_label.place(x=270, y=37, width=60)
        contact_entry = Entry(customer_frame, font=("Times New Roman", 15), relief=GROOVE, bd=2, textvariable=self.contact)
        contact_entry.place(x=340, y=37, width=200)

        # Calc Frame ============================================================
        calc_frame = Frame(self.root3, bd=3, relief=RIDGE)
        calc_frame.place(x=405, y=200, width=267, height=345)
        obj = Calculator(calc_frame)

        # Cart Frame ==============================================================
        cart_frame = Frame(self.root3, bd=3, relief=RIDGE)
        cart_frame.place(x=672, y=200, width=283, height=345)

        self.cart_label = Label(cart_frame, text="Cart\t\tTotal Products:[0]", font=("Times New Roman", 13), bg='lightgray', bd=1, relief=RIDGE)
        self.cart_label.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(cart_frame, orient=VERTICAL)
        scrollx2 = Scrollbar(cart_frame, orient=HORIZONTAL)
        scrollx2.pack(side=BOTTOM, fill=X)
        scrolly2.pack(side=RIGHT, fill=Y)

        self.cart_table = ttk.Treeview(cart_frame, columns=("pid", "name", "qty", "price"), yscrollcommand=scrolly2.set, xscrollcommand=scrollx2.set)
        self.cart_table.heading("pid", text="PID.")
        self.cart_table.heading("name", text="Product")
        self.cart_table.heading("qty", text="Quantity")
        self.cart_table.heading("price", text="Price")

        self.cart_table['show'] = "headings"

        self.cart_table.column("pid", width=90)
        self.cart_table.column("name", width=100)
        self.cart_table.column("qty", width=100)
        self.cart_table.column("price", width=100)

        scrollx2.config(command=self.cart_table.xview)
        scrolly2.config(command=self.cart_table.yview)

        self.cart_table.pack(fill=BOTH, expand=1)

        # Total Frame ======================================================
        total_frame = Frame(self.root3, bd=3, relief=RIDGE)
        total_frame.place(x=405, y=545, width=550, height=140)

        p_name_label = Label(total_frame, text="Product Name", font=("Times New Roman", 15), bg='white')
        p_name_label.place(x=0, y=10, width=130)
        p_name_entry = Entry(total_frame, font=("Times New Roman", 15), relief=RIDGE, bd=2, bg='lightgray', textvariable=self.product_name, state="readonly")
        p_name_entry.place(x=5, y=40, width=200)

        ppq_label = Label(total_frame, text="Price Per Qty", font=("Times New Roman", 15), bg='white')
        ppq_label.place(x=235, y=10, width=130)
        ppq_entry = Entry(total_frame, font=("Times New Roman", 15), relief=RIDGE, bd=2, bg='lightgray', textvariable=self.ppq, state="readonly")
        ppq_entry.place(x=245, y=40, width=130)

        qty_label = Label(total_frame, text="Quantity", font=("Times New Roman", 15), bg='white')
        qty_label.place(x=355, y=10, width=130)
        qty_entry = Entry(total_frame, font=("Times New Roman", 15), relief=RIDGE, bd=2, bg='lightyellow', textvariable=self.qty)
        qty_entry.place(x=385, y=40, width=125)

        self.stock_label = Label(total_frame, text="", font=("Times New Roman", 15), bg='white')
        self.stock_label.place(x=0, y=90, width=190)

        clear_btn = Button(total_frame, text="Clear", font=('Times New Roman', 15), bg="#607d8b", cursor="hand2", fg='white', command=self.clear1)
        clear_btn.place(x=235, y=90, width=130, height=30)

        add_btn = Button(total_frame, text="Add/Update Cart", font=('Times New Roman', 15), bg="orange", cursor="hand2", command=self.add_to_cart)
        add_btn.place(x=375, y=90, width=150, height=30)

        # Bill Frame ============================================================================
        bill_frame = Frame(self.root3, bd=3, relief=RIDGE)
        bill_frame.place(x=955, y=110, width=390, height=400)

        bill_label = Label(bill_frame, text="Customer Billing Area", font=("Goudy Old Style", 20), bg="orange", fg='white')
        bill_label.pack(side=TOP, fill=X)

        bill_scrolly = Scrollbar(bill_frame, orient=VERTICAL)
        bill_scrolly.pack(side=RIGHT, fill=Y)
        bill_scrollx = Scrollbar(bill_frame, orient=HORIZONTAL)
        bill_scrollx.pack(side=BOTTOM, fill=X)

        self.bill_area = Text(bill_frame, font=("Cascadia Code", 10), bg='white', yscrollcommand=bill_scrolly.set, xscrollcommand=bill_scrollx.set, width=220)
        bill_scrolly.config(command=self.bill_area.yview)
        bill_scrollx.config(command=self.bill_area.xview)
        self.bill_area.pack(fill=Y, expand=1)

        # Final Frame ==========================================================================
        final_frame = Frame(self.root3, bd=3, relief=RIDGE)
        final_frame.place(x=955, y=510, width=390, height=175)

        self.label_1 = Label(final_frame, text="Bill Amount\n0", font=("Goudy Old Style", 15), bg='blue', fg='white', bd=3, relief=RAISED)
        self.label_1.place(x=0, y=0, width=120, height=80)

        self.label_2 = Label(final_frame, text="Discount\n5%", font=("Goudy Old Style", 15), bg='green', fg='white', bd=3, relief=RAISED)
        self.label_2.place(x=122, y=0, width=120, height=80)

        self.label_3 = Label(final_frame, text="Net Pay\n0", font=("Goudy Old Style", 15), bg='gray', fg='white', bd=3, relief=RAISED)
        self.label_3.place(x=244, y=0, width=140, height=80)

        print_btn = Button(final_frame, text="Print", font=('Times New Roman', 15), bg="lime", cursor="hand2", bd=2, relief=RAISED, command=self.print_bill)
        print_btn.place(x=0, y=90, width=120, height=60)

        clear_btn2 = Button(final_frame, text="Clear All", font=('Times New Roman', 15), bg="lightgray", cursor="hand2", bd=2, relief=RAISED, command=self.clear_all)
        clear_btn2.place(x=122, y=90, width=120, height=60)

        save_btn = Button(final_frame, text="Generate\nSave Bill", font=('Times New Roman', 15), bg="aqua", cursor="hand2", bd=2, relief=RAISED, command=self.generate_bill)
        save_btn.place(x=244, y=90, width=140, height=60)
        self.show1()
        self.time()

    def show1(self):
        con = sqlite3.connect(database=r"employee_database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM products WHERE status='Active'")
        rows = cur.fetchall()
        self.product_table.delete(*self.product_table.get_children())
        for row in rows:
            self.product_table.insert('', END, values=row)

    def add_to_cart(self):
        con = sqlite3.connect(database=r"employee_database.db")
        cur = con.cursor()
        cur.execute("SELECT pid FROM products WHERE name=?", (self.product_name.get(),))
        rows = cur.fetchone()
        # self.cart_table.delete(*self.cart_table.get_children())
        for row in rows:

            self.list.append([row, self.product_name.get(), self.ppq.get()])
            if self.list.count([row, self.product_name.get(), self.ppq.get()]) > 1:
                c = messagebox.askyesno('Warning!', 'This Item Is Already Present In The Cart.\n Do You Want To Update It?', parent=self.root3)
                if c == True:
                     d = self.cart_table.focus()
                     t = self.cart_table.item(d, values=[row, self.product_name.get(), self.qty.get(), self.ppq.get()])
                     self.manage_qty()

                else:
                    messagebox.showerror('Error!', 'Please Enter A Different Quantity', parent=self.root3)
            else:
                self.list2.append([row, self.product_name.get(), self.qty.get(), self.ppq.get()])
                self.cart_table.insert('', END, values=[row, self.product_name.get(), self.qty.get(), self.ppq.get()])
                self.manage_qty()
                self.cart_label.config(text=f"Cart\t\tTotal Products:[{len(self.list)}]")

    def time(self):
        t = time.strftime("%I:%M:%S %p")
        d = time.strftime("%d/%m/%Y")
        self.clock_label.config(text=f"Admin Dashboard \t\t Date: {d} \t\t Time: {t}")
        self.clock_label.after(200, self.time)

    def get_data(self, ev):
        f = self.product_table.focus()
        content = (self.product_table.item(f))
        row = content['values']
        self.product_name.set(row[3]),
        self.ppq.set(row[4]),
        self.check_status()


    def check_status(self):
        con = sqlite3.connect(r"employee_database.db")
        cur = con.cursor()

        cur.execute("SELECT qty FROM products WHERE name=?", (self.product_name.get(),))
        rows = cur.fetchone()

        if self.product_name.get() != "" and self.qty.get() != "":
            if float(self.qty.get()) <= float(rows[0]):
                self.stock_label.config(text="In Stock", fg='green')
            elif float(self.qty.get()) > float(rows[0]):
                self.stock_label.config(text="Currently Not In Stock", fg='red')
            else:
                self.stock_label.config(text="")
            self.stock_label.after(200, self.check_status)
        else:
            self.stock_label.after(200, self.check_status)

    def clear1(self):
        self.product_name.set("")
        self.qty.set("")
        self.ppq.set("")
        self.stock_label.config(text="")

    def clear_all(self):
        self.product_name.set("")
        self.qty.set("")
        self.ppq.set("")
        self.stock_label.config(text="")
        self.name.set("")
        self.contact.set("")
        self.bill_area.delete('1.0', END)
        self.chk_print = 0
        self.label_1.config(text="Bill Amount\n0")
        self.label_3.config(text="Net Pay\n0")
        self.search_txt.set("")
        self.list.clear()
        self.list2.clear()
        for item in self.cart_table.get_children():
            self.cart_table.delete(item)

    def manage_qty(self):
        con = sqlite3.connect(r"employee_database.db")
        cur = con.cursor()

        cur.execute("SELECT qty FROM products WHERE name=?", (self.product_name.get(),))
        rows = cur.fetchone()
        updated_value = rows[0] - int(self.qty.get())
        cur.execute("UPDATE products SET qty=? WHERE name=?", (updated_value, self.product_name.get(),))
        con.commit()
        self.show1()

    def bill_updates(self):
        self.amount = 0
        self.discount = 0
        self.net_pay = 0

        for row in self.list2:
            self.amount = self.amount + (float(row[2]) * int(row[3]))

        self.discount = ((self.amount * 5) / 100)
        self.net_pay = self.amount - ((self.amount * 5) / 100)
        self.label_1.config(text=f"Bill Amount\n{self.amount}")
        self.label_3.config(text=f"Net Pay\n{self.net_pay}")

    def generate_bill(self):
        filename = time.strftime("%I-%M-%S%p")
        self.bill_top()
        self.bill_middle()
        self.bill_updates()
        self.bill_bottom()
        f = open(f"bills/{filename}.txt", 'w')
        f.write(self.bill_area.get('1.0', END))
        f.close()
        messagebox.showinfo('Successful', 'Bill Generated Successfully!', parent=self.root3)
        self.chk_print = 1

    def bill_top(self):
        invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''
\t\tJagdamba Agencies
\t Phone No. 98725***** , Akot-444101
{str("=" * 45)}
Customer Name: {self.name.get()}
Ph no. :{self.contact.get()}
Bill No. {str(invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("=" * 45)}
Product Name\t\t\tMRP\tAmount
{str("=" * 45)}
        '''
        self.bill_area.delete('1.0', END)
        self.bill_area.insert('1.0', bill_top_temp)

    def bill_middle(self):
        for row in self.list2:
        # pid,name,price,qty,stock
            name = row[1]
            qty = row[3]
            price = float(row[2]) * int(row[3])
            price = str(price)
            self.bill_area.insert(END, "\n " + name + "\t\t\t" + qty + "\tRs." + price)

    def bill_bottom(self):
        bill_bottom_temp = f'''
{str("=" * 45)}
Bill Amount\t\t\t\tRs.{self.amount}
Discount\t\t\t\tRs.{self.discount}
Net Pay\t\t\t\tRs.{self.net_pay}
{str("=" * 45)}\n
\t\tThank You For Shopping!
            '''
        self.bill_area.insert(END, bill_bottom_temp)
        
    def logout(self):
        confirm = messagebox.askyesno('Confirm', 'Do You Really Want To Logout?', parent=self.root3)
        if confirm == True:
            self.root3.destroy()

    def print_bill(self):
        if self.chk_print == 1:
            messagebox.showinfo("Printing", 'Please wait', parent=self.root3)
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.bill_area.get('1.0', END))
            os.startfile(new_file, 'print')
        else:
            messagebox.showerror('Error', 'Please Generate the Bill Before Printing')

    def search(self):
        con = sqlite3.connect(database=r"employee_database.db")
        cur = con.cursor()
        if self.search_txt.get() == "":
            messagebox.showerror('Error!', 'Please provide a search input', parent=self.root3)
        else:
            cur.execute("SELECT * FROM products WHERE " + "name" + " LIKE '%" + self.search_txt.get() + "%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.product_table.delete(*self.product_table.get_children())
                for row in rows:
                    self.product_table.insert('', END, values=row)
            else:
                messagebox.showerror('Error!', 'No Record Found', parent=self.root3)


if __name__ == '__main__':
    root = Tk()
    obj = EmployeeModule(root)
    root.mainloop()