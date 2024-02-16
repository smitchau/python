from tkinter import *
import Tkinter_2 as t

root = Tk()

root.geometry('400x500')
root.title('Registration Form')

Title = Label(root,text='Registration Form',font=('arial',17,'bold'))
Title.pack()

id = Label(root,text='ID',font=('arial',12,'bold'))
id.place(x=50,y=70)

e_id = Entry(root,text='Enter id',bg='blue',fg='white')
e_id.place(x=150,y=70)

name = Label(root,text='First Name',font=('arial',12,'bold'))
name.place(x=50,y=120)

e_name = Entry(root,text='Enter First Name',bg='blue',fg='white')
e_name.place(x=150,y=120)

lname = Label(root,text='Last Name',font=('arial',12,'bold'))
lname.place(x=50,y=170)

e_lname = Entry(root,text='Enter Last Name',bg='blue',fg='white')
e_lname.place(x=150,y=170)

mobile = Label(root,text='Mobile',font=('arial',12,'bold'))
mobile.place(x=50,y=220)

e_mobile = Entry(root,text='Enter mobile number',bg='blue',fg='white')
e_mobile.place(x=150,y=220)

email = Label(root,text='email',font=('arial',12,'bold'))
email.place(x=50,y=270)

e_email = Entry(root,text='Enter email ',bg='blue',fg='white')
e_email.place(x=150,y=270)

password = Label(root,text='password',font=('arial',12,'bold'))
password.place(x=50,y=320)

e_password = Entry(root,text='Enter password ',bg='blue',fg='white')
e_password.place(x=150,y=320)

INSERT = Button(text='Insert',bg='Chocolate',font=('arial',16,'bold'),command=t.login)
INSERT.place(x=40,y=370)

UPDATE = Button(text='UPDATE',bg='Chocolate',font=('arial',16,'bold'))
UPDATE.place(x=140,y=370)

DELETE = Button(text='DELETE',bg='Chocolate',font=('arial',16,'bold'))
DELETE.place(x=270,y=370)

root.mainloop()
