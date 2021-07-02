from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
from employee_module import EmployeeModule
from employee import Employee
from register import Register
from main import Sales
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("920x525+215+105")
        self.root.config(bg='lightyellow')


        self.username = StringVar()
        self.password = StringVar()

        self.bullet = "\u2022"

        self.img = Image.open('images/login1.jpg')
        self.img = self.img.resize((330, 495), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        img_label = Label(self.root, image=self.img)
        img_label.place(x=10, y=10)

        login_frame = Frame(self.root, bd=3, relief=RIDGE)
        login_frame.place(x=500, y=10, width=410, height=510)

        title_label = Label(login_frame, text="Login To The System", font=("Times New Roman", 25, "bold"))
        title_label.place(x=0, y=10, relwidth=1, height=40)

        username_label = Label(login_frame, text="Username", font=("Times New Roman", 15))
        username_label.place(x=50, y=105, width=80, height=30)
        username_entry = Entry(login_frame, font=("Times New Roman", 15), bg="lightgray", bd=2, relief=FLAT, textvariable=self.username)
        username_entry.place(x=50, y=145, width=200, height=28)

        password_label = Label(login_frame, text="Password", font=("Times New Roman", 15))
        password_label.place(x=50, y=203, width=80, height=30)
        password_entry = Entry(login_frame, font=("Times New Roman", 15), bg="lightgray", bd=2, relief=FLAT, textvariable=self.password, show=self.bullet)
        password_entry.place(x=50, y=243, width=200, height=28)

        login_btn = Button(login_frame, text="Login", font=("Times New Roman", 18, "bold"), bg='skyblue', fg='white', cursor="hand2", command=self.login_admin)
        login_btn.place(x=50, y=301, width=300, height=35)

        or_label = Label(login_frame, text="-----------------------OR-----------------------", font=("Times New Roman", 15), bg='white', bd=0, relief=FLAT, fg='lightgray')
        or_label.place(x=0, y=356, relwidth=1)

        register_label = Label(login_frame, text="Register as an Admin", font=("Times New Roman", 12))
        register_label.place(x=50, y=391)
        register_btn = Button(login_frame, text="Register Here", font=("Times New Roman", 12), bg='white', fg='red', cursor="hand2", bd=0, command=self.register)
        register_btn.place(x=190, y=390)

        or_label2 = Label(login_frame, text="-----------------------OR-----------------------", font=("Times New Roman", 15), bg='white', bd=0, relief=FLAT, fg='lightgray')
        or_label2.place(x=0, y=430, relwidth=1)

        forgot_btn = Button(login_frame, text="Forgot Password?", font=("Times New Roman", 12), bg='white', fg='orange', cursor="hand2", bd=0, command=self.forget_pass)
        forgot_btn.place(x=150, y=460)

    def login_admin(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror('Error!', 'Username And Password Are Mandatory')
        else:
            con = sqlite3.connect(r"employee_database.db")
            cur = con.cursor()

            cur.execute("SELECT user_type FROM employees WHERE eid=?", (self.username.get(),))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror('Error!', 'Invalid UserID')
            else:
                if row[0] == "Admin":
                    cur.execute("SELECT password FROM employees WHERE eid=?", (self.username.get(),))
                    row2 = cur.fetchone()
                    print(row2[0])
                    if int(row2[0]) == int(self.password.get()):
                        self.dashboard()
                    else:
                        print(self.password.get())
                        messagebox.showerror('Error!', 'Invalid Password')
                elif row[0] == "Employee":
                    cur.execute("SELECT password FROM employees WHERE eid=?", (self.username.get(),))
                    row2 = cur.fetchone()
                    if int(row2[0]) == int(self.password.get()):
                        self.employ()
                    else:
                        messagebox.showerror('Error!', 'Invalid Password')

    def dashboard(self):
        con = sqlite3.connect(r"employee_database.db")
        cur = con.cursor()
        cur.execute("SELECT name FROM employees WHERE eid=?", (self.username.get(),))
        row = cur.fetchone()
        messagebox.showinfo('Success', f"Welcome {row[0]}", parent=self.root)
        self.new_win = Toplevel(self.root)
        self.new_obj = Sales(self.new_win)
        self.username.set("")
        self.password.set("")

    def employ(self):
        con = sqlite3.connect(r"employee_database.db")
        cur = con.cursor()
        cur.execute("SELECT name FROM employees WHERE eid=?", (self.username.get(),))
        row = cur.fetchone()
        messagebox.showinfo('Success', f"Welcome {row[0]}", parent=self.root)
        self.new_win = Toplevel(self.root)
        self.new_obj = EmployeeModule(self.new_win)
        self.username.set("")
        self.password.set("")

    def register(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Register(self.new_win)

    def forget_pass(self):
        win = Toplevel(self.root)
        win.title('Change Password')
        win.geometry("400x350+500+100")
        for_label = Label(win, text='Email Verification', font=('Times New Roman', 20, 'bold'), bg='blue', fg='white')
        for_label.place(x=0, y=0, relwidth=1)
        win.focus_force()

        otp_label = Label(win, text='Enter OTP sent on registered Email ID', font=('Times New Roman', 15))
        otp_label.place(x=20, y=60)
        otp_entry = Entry(win, font=('Times New Roman', 15), relief=RIDGE, bd=2)
        otp_entry.place(x=20, y=100)

        confirm_btn = Button(win, text='Confirm', font=('Times New Roman', 15), relief=RAISED, bd=2, bg='lightblue', cursor='hand2')
        confirm_btn.place(x=230, y=100, width=120, height=30)

        new_pass_label = Label(win, text='Enter New Password', font=('Times New Roman', 15))
        new_pass_label.place(x=20, y=140)
        new_pass_entry = Entry(win, font=('Times New Roman', 15), relief=RIDGE, bd=2)
        new_pass_entry.place(x=20, y=170)

        confirm_pass_label = Label(win, text='Confirm New Password', font=('Times New Roman', 15))
        confirm_pass_label.place(x=20, y=210)
        confirm_pass_entry = Entry(win, font=('Times New Roman', 15), relief=RIDGE, bd=2)
        confirm_pass_entry.place(x=20, y=240)

        submit_btn = Button(win, text='Submit', font=('Times New Roman', 15), relief=RAISED, bd=2, bg='green', cursor='hand2')
        submit_btn.place(x=130, y=290, width=120, height=30)

if __name__ == '__main__':
    root = Tk()
    obj = Login(root)
    root.mainloop()