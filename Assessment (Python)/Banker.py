#===============================Banker Module===============================

#import module
import datetime
now = datetime.datetime.now()

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

# Initialize an empty dictionary to store accounts

accounts = {}

#========Add_customer============

def add_customer():
    # Getting user input for account details
    num_accounts = int(input("Enter the number of accounts: "))

    for _ in range(num_accounts):
        acc_number = input("Enter account number: ")
        name = input("Enter name: ")
        balance = float(input("Enter balance: "))
        times = str(now)
    
        # Creating a dictionary for the account
        account_info = {'name': name, 'balance': balance ,'Opening-Date': times}
        
        # Adding the account to the accounts dictionary
        accounts[acc_number] = account_info

    # Printing the accounts dictionary
    print(accounts)
    print('customer is added...')

    with open('banker.txt','w') as file:
        file.write(str(accounts))
#========View_customer============

def View_Customer():
    with open('banker.txt','r') as file:
        print(file.readline())
      
        
#======Search Customer============

def search_acc():
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


#======view all Customer============

def View_All_Customer():
    with open('banker.txt','r') as file:
        lines = file.readlines()
        for item in lines:
            print(item)

#======Total Customer============
     
def Total_Amounts():
    with open('banker.txt','r') as file:
        data = file.readline()

        content = eval(data)


    total_balance = 0

    total_balance = sum(customer['balance'] for customer in content.values())

    print(f"The total balance across all customers is: {total_balance}")

