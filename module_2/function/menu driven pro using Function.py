def menu():

    status = True
    global total
    total=0
    while status:

        print("\n============Welcome To Tops Restaurent=============")

        print("\tSrno \tItem \t\tPrice")
        print("\t1 \tPizza \t\t90/-")
        print("\t2 \tBurgur \t\t89/-")
        print("\t3 \tPani-Puri \t100/-")
        print("\t4 \tDosa \t\t80/-")

        choice = int(input("\nEnter choice :"))
        
        if choice == 1:
            print("\nyour Item : Pizza")
            quantity = int(input("Enter Quantity : "))
            t1 = quantity * 90
            total=total + t1
            print("Total Price : ",t1 ,"rs.")
            
        elif choice == 2:
            print("\nyour Item : Burgur")
            quantity = int(input("Enter Quantity : "))
            t2 = quantity * 89
            total=total + t2
            print("Total Price : ",t2 ,"rs.")
        elif choice == 3:
            print("\nyour Item : Pani-Puri")
            quantity = int(input("Enter Quantity : "))
            t3 = quantity * 100
            total=total + t3
            print("Total Price : ",t3 ,"rs.")
            
        elif choice == 4:
            print("\nyour Item : Dosa")
            quantity = int(input("Enter Quantity : "))
            t4 = quantity * 80
            total=total + t4
            print("Total Price : ",t4 ,"rs.")
            
        else:
            print("Please select valid choice")
            
        choice1 = input("\ndo you want to continue ? :[y/n]")
     
        if choice1 == 'y':
            status = True
        else:
            status = False
            
            print("total is : ",total)


menu()
