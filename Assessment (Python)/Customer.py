import Banker as b1         #import banker file b1

#====create Customer_menu===========
def Customer_menu():

    print("\nWelcome to Customers's App")
    print("\n\t\tOperations Menu")
    print("\n\t\t1) Withdraw Amount")
    print("\t\t2) Deposite Amount")
    print("\t\t3) view Balance")

#==========Withdraw_Amount================
def Withdraw_Amount():
    ac_no  = input('Enter ac no : ')
    name = input('Enter name : ')
    Amount = int(input('Enter Amount : '))

    var = b1.dic1[ac_no]['balance'] - Amount

    b1.dic1[ac_no] = {'name':name,'balance':var}

    print(b1.dic1)

#================Deposite_Amount=================
def Deposite_Amount():
    ac_no  = input('Enter ac no : ')
    name = input('Enter name : ')
    Amount = int(input('Enter Amount : '))

    var = b1.dic1[ac_no]['balance'] + Amount

    b1.dic1[ac_no] = {'name':name,'balance':var}

    print(b1.dic1)
    
#=========view_balance=============
def view_balance():
    ac_no  = input('Enter ac no : ')

    print('Your Balance is : ',b1.dic1[ac_no]['balance'])

