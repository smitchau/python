'''
 Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30.
'''
li = []  # Empty list to store user input numbers
l2 = []  # Empty list to store squares of user input numbers

choice = int(input("how many total numbers you want to enter: "))  # Taking input for the total number of values
for i in range(choice):
    no = int(input("Enter number: "))  # Taking user input for each number
    li.append(no)  # Appending the number to 'li'
    l2.append(no ** 2)  # Appending the square of the number to 'l2'

print('list:', li)  # Printing the list of entered numbers
print('\nfirst 5 value squares:', l2[:5])  # Printing squares of the first 5 values
print('\nlast 5 value squares:', l2[-5:])  # Printing squares of the last 5 values


      
