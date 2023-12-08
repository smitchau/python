#Write a Python function to check whether a number is in a given range

def number(num):
    # Iterate from 1 up to the given number (inclusive) with a step of 2
    # This step of 2 ensures that only odd numbers are considered
    for i in range(1, num + 1, 2):
        # Print each odd number in the range
        print(i)

# Take user input for the number
num = int(input("Enter number: "))

# Call the number function with the user-input number as an argument
number(num)
