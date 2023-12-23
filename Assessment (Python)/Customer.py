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
    acc_number = input("\n Enter Account number : ")

    try:
        with open('banker.txt','r') as file:
            content = file.read()
            if content:
                data = eval(content)
                current_name = data.get(acc_number,{}).get("name",0)
                current_balance = data.get(acc_number,{}).get("balance",0)
                
    except FileNotFoundError:
        current_name= 0
        current_balance=0
        
    withdraw_amount = int(input("Enter withdraw amount : "))

    new_name = current_name
    
    new_balance = current_balance - withdraw_amount

    data[acc_number] = {'name':new_name , 'balance':new_balance}

    with open('banker.txt','w') as file:
        file.write(str(data))

#================Deposite_Amount=================
def Deposite_Amount():
    acc_number = input("\n Enter Account number : ")

    try:
        with open('banker.txt','r') as file:
            content = file.read()
            if content:
                data = eval(content)
                current_name = data.get(acc_number,{}).get("name",0)
                current_balance = data.get(acc_number,{}).get("balance",0)
                
    except FileNotFoundError:
        current_name= 0
        current_balance=0
        
    deposite_amount = int(input("Enter deposite amount : "))

    new_name = current_name
    
    new_balance = current_balance + deposite_amount

    data[acc_number] = {'name':new_name , 'balance':new_balance}

    with open('banker.txt','w') as file:
        file.write(str(data))
  
#=========view_balance=============
def view_balance():
    with open('banker.txt','r') as file:
        data = file.readline()

        content = eval(data)
    
        # Get user input for the search key
        search_key = input("\nEnter the key to search for: ")

        # Initialize an empty dictionary for the desired dictionary
        desired_dict = {}

        # Search for the dictionary with the user-provided key
        for item in content.items():
            if search_key in item:
                desired_dict = item
                break

        if desired_dict:
            print('\n',desired_dict)
        else:
            print(f"Dictionary with key '{search_key}' not found.")
