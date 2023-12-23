import Banker as b1        #import banker modul b1
import Customer as c1      #import customer modul c1
#===create role sunction====
def role_menu():
    
    #===Display menu role====
    print('\n\t\t   WELCOME TO PYTHON BANK MANAGEMENT SYSTEM')
    print('\n\t\t   Select your role')
    print('\n\t\t\t1) Banker')
    print('\t\t\t2) Customer')
    print('\n\t\t\t3)Exit')

    choice = int(input('Choose your role :'))      #role choice input
    bool = True       #variable bool True
    
    #===========================choice (1) for banker=================================

    if(choice == 1):
        
        #=======while loop========
        while bool:

            b1.display()   #Banker display function call

            operation = int(input('\nEnter operation which you want to perform :'))
            
            #======Add customer operation perform==========
            if operation == 1:
                b1.add_customer()

                more_oper = input('\nDo you want to perform more operations press "y" for yes and press "n" for no :')

                if (more_oper == 'y'):     #user input yes continue operation perform
                    bool = True
                        
                elif(more_oper == 'n'):    #user input no exit
                    bool = False

            #======View customer operation perform==========

            elif operation == 2:
                b1.View_Customer()

                more_oper = input('\nDo you want to perform more operations press "y" for yes and press "n" for no :')

                if (more_oper == 'y'):
                    bool = True
                        
                elif(more_oper == 'n'):
                    bool = False

            #======search customer operation perform==========

            elif operation == 3:

                
                b1.search_acc()

                more_oper = input('\nDo you want to perform more operations press "y" for yes and press "n" for no :')

                if (more_oper == 'y'):
                    bool = True
                        
                elif(more_oper == 'n'):
                    bool = False

             #======view all customer operation perform==========

            elif operation == 4:
                
                b1.View_All_Customer()

                more_oper = input('\nDo you want to perform more operations press "y" for yes and press "n" for no :')

                if (more_oper == 'y'):
                    bool = True
                        
                elif(more_oper == 'n'):
                    bool = False
                    
            elif operation == 5:
                
                b1.Total_Amounts()

                more_oper = input('\nDo you want to perform more operations press "y" for yes and press "n" for no :')

                if (more_oper == 'y'):
                    bool = True
                        
                elif(more_oper == 'n'):
                    bool = False

#================choice (2) for customer===============================================

    elif(choice == 2):
        
        bool = True       #variable bool True
        
        #=======while loop========
        while bool:

            c1.Customer_menu()   #Banker display function call

            operation = int(input('\nEnter operation which you want to perform :'))
            
            #======Add Withdraw amount operation perform==========
            if operation == 1:
                c1.Withdraw_Amount()

                more_oper = input('\nDo you want to perform more operations press "y" for yes and press "n" for no :')

                if (more_oper == 'y'):     #user input yes continue operation perform
                    bool = True
                        
                elif(more_oper == 'n'):    #user input no exit
                    bool = False

            #======View deposite amout operation perform==========

            elif operation == 2:
                c1.Deposite_Amount()

                more_oper = input('\nDo you want to perform more operations press "y" for yes and press "n" for no :')

                if (more_oper == 'y'):
                    bool = True
                        
                elif(more_oper == 'n'):
                    bool = False

            #======View balance operation perform==========

            elif operation == 3:
                
                c1.view_balance()

                more_oper = input('\nDo you want to perform more operations press "y" for yes and press "n" for no :')

                if (more_oper == 'y'):
                    bool = True
                        
                elif(more_oper == 'n'):
                    bool = False


    #==================================choice (3) for Exit=================================

    elif(choice == 3):
        exit()

    #other wise else part invalide choice
    else:
        print('Enter valid Choice....')

role_menu() #call role_menu
