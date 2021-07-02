from tkinter import *
from tkinter import messagebox


class Calculator:
    def __init__(self, calc_frame1):
        self.calc_frame1 = calc_frame1

        self.expression = ""
        self.equation = StringVar()

        input_field = Entry(self.calc_frame1, textvariable=self.equation, font=("Times New Roman", 15), bd=5, relief=SUNKEN)
        input_field.place(x=0, y=0, height=40, relwidth=1)



        self.equation.set("")

        btn_1 = Button(self.calc_frame1, text='1', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number(1), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_1.place(x=0, y=40, height=70, width=65)
        btn_2 = Button(self.calc_frame1, text='2', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number(2), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_2.place(x=65, y=40, height=70, width=65)
        btn_3 = Button(self.calc_frame1, text='3', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number(3), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_3.place(x=130, y=40, height=70, width=65)
        btn_4 = Button(self.calc_frame1, text='4', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number(4), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_4.place(x=0, y=110, height=70, width=65)
        btn_5 = Button(self.calc_frame1, text='5', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number(5), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_5.place(x=65, y=110, height=70, width=65)
        btn_6 = Button(self.calc_frame1, text='6', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number(6), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_6.place(x=130, y=110, height=70, width=65)
        btn_7 = Button(self.calc_frame1, text='7', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number(7), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_7.place(x=0, y=180, height=70, width=65)
        btn_8 = Button(self.calc_frame1, text='8', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number(8), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_8.place(x=65, y=180, height=70, width=65)
        btn_9 = Button(self.calc_frame1, text='9', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number(9), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_9.place(x=130, y=180, height=70, width=65)
        btn_0 = Button(self.calc_frame1, text='0', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number(0), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_0.place(x=0, y=250, height=88, width=65)
        #
        btn_plus = Button(self.calc_frame1, text='+', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number('+'), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_plus.place(x=195, y=40, height=70, width=65)
        btn_minus = Button(self.calc_frame1, text='-', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number('-'), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_minus.place(x=195, y=110, height=70, width=65)
        btn_multiply = Button(self.calc_frame1, text='*', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number('*'), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_multiply.place(x=195, y=180, height=70, width=65)
        btn_divide = Button(self.calc_frame1, text='/', fg='black', bg='lightgray', bd=3, command=lambda: self.input_number('/'), relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_divide.place(x=195, y=250, height=88, width=65)
        btn_equal = Button(self.calc_frame1, text='=', fg='black', bg='lightgray', bd=3, command=self.evaluate, relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_equal.place(x=130, y=250, height=88, width=65)
        btn_clear = Button(self.calc_frame1, text='C', fg='black', bg='lightgray', bd=3, command=self.clear_input, relief=RAISED, font=("Times New Roman", 10, "bold"))
        btn_clear.place(x=65, y=250, height=88, width=65)

    def input_number(self, number):
        self.expression = self.expression + str(number)
        self.equation.set(self.expression)

    def clear_input(self):
        self.expression = ""
        self.equation.set("")

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.equation.set(result)
            self.expression = ""
        except:
            messagebox.showerror('Error!', 'Please Enter A Valid Equation')
            self.expression = ""

if __name__ == '__main__':
    calc_frame1 = Tk()
    obj = Calculator(calc_frame1)
    calc_frame1.mainloop()