from tkinter import *
def login():

    root = Tk()

    root.geometry('400x300')
    root.title('Login Form')

    Title = Label(root,text='Login Form',font=('arial',17,'bold'))
    Title.pack()

    email = Label(root,text='email',font=('arial',12,'bold'))
    email.place(x=50,y=70)

    e_email = Entry(root,text='Enter email ',bg='blue',fg='white')
    e_email.place(x=150,y=70)

    mobile = Label(root,text='Mobile',font=('arial',12,'bold'))
    mobile.place(x=50,y=120)

    e_mobile = Entry(root,text='Enter mobile number',bg='blue',fg='white')
    e_mobile.place(x=150,y=120)

    password = Label(root,text='password',font=('arial',12,'bold'))
    password.place(x=50,y=170)

    e_password = Entry(root,text='Enter password ',bg='blue',fg='white')
    e_password.place(x=150,y=170)

    Login = Button(root ,text='Login',bg='Chocolate',font=('arial',16,'bold'))
    Login.place(x=170,y=230)

    root.mainloop()

