class Order_menu:
    
    def __init__(self):
        print('\n\t\t\tWelcome to Amazing Pizza and Pasta Pizzeria')
        print('\n\t\t\t\tpress 1 : order menu')
        print('\t\t\t\tpress 2 : Exit')

    def choice(self):
        choice = int(input('\nEnter Your choice :'))
        loop = True
        total_pizza_price = 0
        total_pasta_price = 0
        Quantity = 0
        pizza_counter = 0
        pasta_counter1 = 0
        pasta_counter2 = 0
        
        if choice == 1:
            while loop:
                print('\n\t1 large pizza = 10.99 AUD')
                print('\n\t***Buy 4 or more pizza and get 1.5lt of soft drink free***')

                print('\n\n\t1 large pasta = 9.5 AUD')
                print('\n\t***Buy 4 or more pastas and get 2 bruschetta free.***')
                print('\n\t***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.')

                print('\n-----------------------------------------------------------------------------------------------------')
                
                name = input("\nEnter your name : ")
                print(f"\nWelcome, {name}")

                pizza_quantities = int(input('\nEnter number or pizza order you want  :'))
                Quantity += pizza_quantities
                pizza_price = pizza_quantities * 10.99
                total_pizza_price += pizza_price
                print('\n\tyour pizza order amount is : ',pizza_price )

                if pizza_quantities >= 4 :
                    pizza_counter += 1
                    print('\n\t\t\t*** Congratulations !! 1.5lt softdrink free *** ') 

                pasta_quantities = int(input('\nEnter number or pasta order you want  :'))
                Quantity += pasta_quantities
                pasta_price = pasta_quantities * 9.5
                total_pasta_price += pasta_price
                print('\n\tyour pasta order amount is : ',pasta_price)

                if pasta_quantities >= 4:
                    pasta_counter1 +=1
                    print('\n\t\t\t*** Congratulations !! get 2 bruschetta free ***  ')

                    if pizza_quantities>= 4:
                        print('\n\t\t\t*** Congratulations !! get 2 chocco brownies ice cream free ***')
                        pasta_counter2 +=1
                        
                    else:
                        pass
               
                print('\n\tyour total order is :  ',pizza_price + pasta_price)

                print('\n-----------------> your Net order amount of the day is :  ',pizza_price + pasta_price)


                reapeat =input('\nwant to enter order from another customer (Y/N) :')

                if reapeat == 'Y' :
                    loop = True

                elif reapeat == 'N':
                    loop = False

                else:
                    exit()
                    
            print('\n------------------Pizza and pasta Bill -----------------------')
            print('\n\npayment received from pizza :  ',total_pizza_price)
            print('\npayment received from pasta :  ',total_pasta_price)
            print('\npayment received today :',total_pizza_price+total_pasta_price)
            print('\nNumber of pizza and pasta sold in one shift : ',Quantity)
            print('\nNumber of 1.5lt soft drink bottles given :',pizza_counter)
            print('\nNumber of bruschetta given to customer : ',pasta_counter1)
            print('\nNumber of chocco brownies ice cream given to customer : ',pasta_counter2)
            print('\nBye Bye !!!')
                
        elif choice == 2:
            exit()

        else:
            exit()
                    
o1 = Order_menu()
o1.choice()
