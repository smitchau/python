#======================================Banker Module===============================

#========Display============

def display():
    
    #======Display Menu======
            
    print("Welcome to Banker's App\n")
    print("\t\tOperation Menu\n")
    print("\t\t1) Add Customer")
    print("\t\t2) View Customer")
    print("\t\t3) Search Customer")
    print("\t\t4) View All Customer")
    print("\t\t5) Total Amounts in Bank\n")

dic1 = {'101': {'name': 'smit', 'balance': 20000},'105': {'name': 'nik', 'balance': 5000}}
#========Add_customer============

def add_customer():

    size = int(input("How many customer you want to enter :"))

    for i in range(size):
        ac_no = input("\nEnter Acount number : ")
        
        dic1[ac_no] = {}
        customer_name = input("Enter customer name : ")
        balance = int(input("Enter opening balance : "))

        dic1[ac_no]['name'] = customer_name
        dic1[ac_no]['balance'] = balance
        print('customer is added...')
        

#========View_customer============

def View_Customer():
    print(dic1)

#======Search Customer============

def search_customer():
    ac_no = input("\nEnter Acount number : ")
    print('Customer details is : ',dic1[ac_no])
    
'''
display()
add_customer()
View_Customer()
search_customer()
'''
