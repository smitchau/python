import pymysql

class connection:

    mydb = pymysql.connect(host = "localhost",user = "root" ,password = "")

    mycursor = mydb.cursor()

    mycursor.execute("create database if not exists BankingSystem")

    mydb = pymysql.connect(host = "localhost",user = "root" ,password = "" , database = "BankingSystem")

    mycursor = mydb.cursor()

    mycursor.execute("create table if not exists bank (Ac_no int primary key , name varchar(20) , balance int) ")

    mydb.commit()

class banker(connection):
    
    def __init__(self):
        
        #======Display Menu======
                
        print("Welcome to Banker's App\n")
        print("\t\tOperation Menu\n")
        print("\t\t1) Add Customer")
        print("\t\t2) View Customer")
        print("\t\t3) Search Customer")
        print("\t\t4) View All Customer")
        print("\t\t5) Total Amounts in Bank\n")

        self.mydb = pymysql.connect(host='localhost',user='root',password='',database='BankingSystem')
        self.mycursor = self.mydb.cursor()


    def add_customer(self):
    
        print("-------------------- ADD CUSTOMER ------------------------")
        Ac_no = int(input("Enter Account number : "))
        name = input("Enter Name : ")
        balance = int(input("Enter Balance : "))

        args = (Ac_no,name,balance)
        query = "insert into bank (Ac_no,name,balance) values (%s,'%s',%s) "

        self.mycursor.execute(query % args)

        self.mydb.commit()
       
    #========View_customer============

    def View_Customer(self):
        Ac_no = int(input("Enter Your Account number :"))
        query="select * from bank where Ac_no= %s "
        args = (Ac_no)

        self.mycursor.execute(query % args)
        res = self.mycursor.fetchone()
        print("Customer is :",res[1])          
            
    #======Search Customer============

    def search_acc(self):
        Ac_no = int(input("Enter Your Account number :"))
        query="select * from bank where Ac_no= %s "
        args = (Ac_no)

        self.mycursor.execute(query % args)
        res = self.mycursor.fetchone()
        print("Customer details :",res[0],res[1],res[2])

    #======view all Customer============

    def View_All_Customer(self):
        print("-------------------- DISPLAY All Customer ------------------------")
        self.mycursor.execute("select * from bank")
        res = self.mycursor.fetchall()
        for x in res:
            print(x)
        self.mydb.commit()

    #======Total Customer============
         
    def Total_Amounts(self):
        print("-------------------- Total_Amounts ------------------------")
        balance = 0
        self.mycursor.execute("select * from bank")
        res = self.mycursor.fetchall()
        for x in res:
            balance = balance + x[2]
        print("Total Amount is :",balance)
        self.mydb.commit()

class customer(connection):

    def __init(self):

        print("\nWelcome to Customers's App")
        print("\n\t\tOperations Menu")
        print("\n\t\t1) Withdraw Amount")
        print("\t\t2) Deposite Amount")
        print("\t\t3) view Balance")

        self.mydb = pymysql.connect(host='localhost',user='root',password='',database='BankingSystem')
        self.mycursor = self.mydb.cursor()

    def Withdraw_Amount(self):
        Ac_no = int(input("Enter Your Account number :"))
        amount = int(input("Enter withdraw amount :"))
        query="select * from bank where Ac_no = %s "
        args = (Ac_no)        
        self.mycursor.execute(query % args)
        res = self.mycursor.fetchone()

        balance = res[2] - amount
        
        query ="update bank set balance = %s where Ac_no = %s "
        args = (balance,Ac_no)
        self.mycursor.execute(query % args )
        self.mydb.commit()
        
    #================Deposite_Amount=================
    def Deposite_Amount(self):
        Ac_no = int(input("Enter Your Account number :"))
        amount = int(input("Enter withdraw amount :"))
        query="select * from bank where Ac_no = %s "
        args = (Ac_no)        
        self.mycursor.execute(query % args)
        res = self.mycursor.fetchone()

        balance = res[2] + amount
        
        query ="update bank set balance = %s where Ac_no = %s "
        args = (balance,Ac_no)
        self.mycursor.execute(query % args )
        self.mydb.commit()
      
    #=========view_balance=============
    def view_balance(self):
        Ac_no = int(input("Enter Your Account number :"))
        query="select * from bank where Ac_no= %s "
        args = (Ac_no)

        self.mycursor.execute(query % args)
        res = self.mycursor.fetchone()
        print("Balance is :",res[2]) 

connection = connection()
customer = customer()
customer.view_balance()

