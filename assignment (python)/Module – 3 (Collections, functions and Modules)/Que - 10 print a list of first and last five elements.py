'''
 Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30.
'''
li = []
l2 = []

choice = int(input("how many total number you want to enter : "))
for i in range(choice):
    no = int(input("Enter number : "))
    li.append(no)
    l2.append(no**2)

print('list : ',li)
print('\nfirst 5 value square',l2[:5])
print('\nlast 5 value square',l2[5:])

      
