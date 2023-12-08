from tkinter import Tk,Label,Entry,Button
from tkinter import messagebox as msg

obj = Tk()

obj.title("My calculator")
obj.geometry('400x400')
obj.resizable(False,False)

def Addition():
    add = e_num1.get() + e_num2.get()
    #print('Addition : ',add)
    msg.showinfo('Title',add)
    
def subtraction():
    sub = e_num1.get() + e_num2.get()
    msg.showinfo('Title',sub)

def multyplication():
    mul = e_num1.get() + e_num2.get()
    msg.showinfo('Title',mul)
    
def division():
    div = e_num1.get() + e_num2.get()
    msg.showinfo('Title',div)

    
heading = Label(obj,text='Welcome To Calculator' ,bg='black',fg='white' ,font=('Arial 12 bold'))
heading.place(x=100,y=40)

num1 = Label(obj,text='Enter nuber1 : ',font=('Arial 12 bold'))
num1.place(x=50,y=120)

num2 = Label(obj,text='Enter nuber2 : ',font=('Arial 12 bold'))
num2.place(x=50,y=160)

e_num1 = Entry(obj,)
e_num1 = Entry(obj,)
e_num1.place(x=180,y=120)

e_num2 = Entry(obj,)
e_num2.place(x=180,y=160)

Add = Button(obj,text = "Add" , command = Addition)
Add.place(x=50,y=240)

sub = Button(obj,text = "sub" , command = subtraction)
sub.place(x=120,y=240)

multy = Button(obj,text = "multy" , command = multyplication)
multy.place(x=180,y=240)

div = Button(obj,text = "div" , command = division)
div.place(x=260,y=240)
