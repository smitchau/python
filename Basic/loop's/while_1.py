import random

lucky_num=random.randint(1,100)

print(lucky_num)

status=True
c=1
while c<=5 and status:

    print("Chance: ",c)
    choice=int(input("Enter your guess : "))

    if choice==lucky_num:
        print("You won ")
        status=False
    elif choice>lucky_num:
        print("hint : think lesser number")
    elif choice<lucky_num:
        print("hint : think higher number")

    c+=1
    
    if c>5:
        con=input("Do you want to continue ? :")
        if con=='y':
            c=1
            status=True
        else:
            status=False

    
