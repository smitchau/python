# Write a Python program to convert a tuple to a string. 

tuple_Items = ('p', 'y', 't', 'h', 'o', 'n')  # Given tuple of characters

'''
Method one: Using the 'join' method to concatenate the characters into a string
# Joining the characters using an empty string as a separator and printing the result
print(''.join(tuple_Items))
'''

# Method two: Iterating through the tuple and printing each character without a newline
for i in tuple_Items:
    print(i, end='')  # Printing each character without a newline using 'end=' argument


