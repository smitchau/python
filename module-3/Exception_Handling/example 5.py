'''

try : the code may have any problematic conditions goes inside this block

except : if try can not run successfully then this will run by default

else : if try will execute then this else also

finally : it will execute every time irrespective of any

'''

# ex1

try:
    num = int(input('Enter num : '))
except:
    print("Invalid input")
else:
    print(num * num)
finally:
    print('THANK YOU FOR USING THIS APPLICATIONS')

# ex2

try:
    num1=int(input("Enter num 1: "))
    num2=int(input("Enter num 2: "))
    print("Div : ",num1/num2)
except ZeroDivisionError as z:
    print("Error : ",z)
except ValueError as v:
    print("Error : ",v)
except NameError as n:
    print("Error : ",n)
else:
    print("try block Runnnnnnnnnnnnnnnn")
finally:
    print("Finally block")












    
