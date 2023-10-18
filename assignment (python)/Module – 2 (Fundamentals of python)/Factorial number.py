
num = int(input("Enter last digit number :"))

fact = 1

if num < 0:
    print("Sorry,factorial does not exist for nagative numbers")

elif num == 0:
    print("number is zero")

else: 
    for i in range(1,num + 1):
        fact = fact * i

    print("Factoial of",num,"is",fact)
    
