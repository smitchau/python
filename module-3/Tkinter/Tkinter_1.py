'''
Tkinter : Library in python for GUI

tkinter : module to get the GUI element
'''

from tkinter import Tk,Label

#Tk : class for tkinter module

#object creation of Tk class

obj = Tk()
 
obj.title("My Tkinter Window")
obj.geometry('400x400')
obj.resizable(False,False)

#to write any text on window use lable class

heading = Label(obj , text='Wrlcome to sports club',bg = 'black',fg = 'white' , font = 'arial 15 bold')
heading.place(x=100,y=40)
