'''
Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings
'''

l1 = ['abc', 'bab', 'xyz', '1001', 'c2c']  # List of strings

count = 0  # Initialize a counter to count strings meeting the condition

# Iterate through each word in the list
for word in l1:
    # Check if the length of the word is greater than 2 and the first character is equal to the last character
    if len(word) > 2 and word[0] == word[-1]:
        count += 1  # Increment the count if the condition is met
    else:
        count  # No change to count if the condition is not met, just here for clarity

# Print the count of strings where the first and last characters are the same
print("same first and last character string is:", count)
