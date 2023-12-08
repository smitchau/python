'''
Write a Python function to calculate the factorial of a number
(a nonnegative integer)

'''

def factorial(num):
    # Initialize fact as 1, as the factorial of 0 and 1 is 1
    fact = 1
    
    # Iterate from 1 to the given number (inclusive) using a for loop
    for i in range(1, num + 1):
        # Update fact by multiplying it with the current value of i
        fact = fact * i

    # Print the factorial of the given number
    print(fact)

# Take

