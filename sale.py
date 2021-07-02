from tkinter import *
from tkinter import StringVar
from PIL import ImageTk, Image
import os
from tkinter import messagebox



class Sale:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1120x485+215+135")
        self.root.title("View Bills")
        self.root.config(bg="white")
        self.root.focus_force()

        self.inv_no = StringVar()
        self.bill_list = []

        main_label = Label(self.root, text="Customer Bill Reports", font=("Goudy Old Style", 30, "bold"), bg="#0f4d7d", fg="white")
        main_label.place(x=0, y=0, relwidth=1, height=45)

        invoice_label = Label(self.root, text="Enter Invoice No.", font=("Goudy Old Style", 15))
        invoice_label.place(x=10, y=65, width=180)

        invoice_entry = Entry(self.root, font=("Goudy Old Style", 15), bd=2, bg="lightyellow", textvariable=self.inv_no)
        invoice_entry.place(x=190, y=65, width=250)

        search_btn = Button(self.root, text="Search", font=("Goudy Old Style", 15), cursor="hand2", bg="#33bbf9", fg="white", command=self.search)
        search_btn.place(x=450, y=65, width=100, height=30)

        clear_btn = Button(self.root, text="Clear", font=("Goudy Old Style", 15), cursor="hand2", bg="#607d8b", fg="white", command=self.clear)
        clear_btn.place(x=560, y=65, width=100, height=30)

        list_frame = Frame(self.root, bd=2, relief=RIDGE)
        list_frame.place(x=10, y=105, width=225, height=375)

        list_scrolly = Scrollbar(list_frame, orient=VERTICAL)
        list_scrolly.pack(side=RIGHT, fill=Y)

        self.sales_list = Listbox(list_frame, yscrollcommand=list_scrolly.set)
        list_scrolly.config(command=self.sales_list.yview)
        self.sales_list.bind("<ButtonRelease-1>", self.get_data)
        self.sales_list.pack(fill=BOTH, expand=1)


        bill_frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_frame.place(x=245, y=105, width=390, height=380)

        bill_label = Label(bill_frame, text="Customer Billing Area", font=("Goudy Old Style", 20), bg="orange",
                           fg='white')
        bill_label.pack(side=TOP, fill=X)

        bill_scrolly = Scrollbar(bill_frame, orient=VERTICAL)
        bill_scrolly.pack(side=RIGHT, fill=Y)
        bill_scrollx = Scrollbar(bill_frame, orient=HORIZONTAL)
        bill_scrollx.pack(side=BOTTOM, fill=X)

        self.bill_area = Text(bill_frame, font=("Cascadia Code", 10), bg='white', yscrollcommand=bill_scrolly.set,
                              xscrollcommand=bill_scrollx.set, width=220)
        bill_scrolly.config(command=self.bill_area.yview)
        bill_scrollx.config(command=self.bill_area.xview)
        self.bill_area.pack(fill=Y, expand=1)


        self.img = Image.open('images/img3.jpg')
        self.img = self.img.resize((360, 365), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        img_label = Label(self.root, image=self.img)
        img_label.place(x=745, y=105)
        self.show()


    def show(self):
        self.sales_list.delete(0, END)
        for i in os.listdir('bills'):
            if i.split('.')[1] == 'txt':
                self.sales_list.insert(END, i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self, ev):
        f = self.sales_list.curselection()
        file_name = self.sales_list.get(f)
        row = open(f'bills/{file_name}', 'r')
        self.bill_area.delete('1.0', END)
        self.bill_area.insert('1.0', row.read())

    def search(self):
        if self.inv_no.get() == "":
            messagebox.showerror('Error', 'Please Enter The Invoice No.')
        else:
            if self.inv_no.get() in self.bill_list:
                row2 = open(f'bills/{self.inv_no.get()}.txt', 'r')
                for j in row2:
                    self.bill_area.insert(END, j)
            else:
                messagebox.showerror('Error!', 'Record Not Found')

    def clear(self):
        self.bill_area.delete('1.0', END)
        self.inv_no.set("")


if __name__ == '__main__':
    root = Tk()
    obj = Sale(root)
    root.mainloop()