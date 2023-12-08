'''
 Write a Python function that checks whether a passed string is 
palindrome or not
'''

def palindrome(string):
    # Check if the first character of the string is equal to the last character
    if string[0] == string[-1]:
        print("The passed string is a palindrome")
    else:
        print("The passed string is not a palindrome")


# Take user input for the string
string = input("Enter String: ")
# Call the palindrome function with the user-input string as an argument
palindrome(string)

