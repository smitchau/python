from tkinter import Tk,Label

obj = Tk()
obj.title('Tkinter Practice Program')
obj.geometry('400x500')
obj.resizable(False,False)

heading = Label(obj,text='Hello Tkinter')
heading.place(x=50,y=40)



