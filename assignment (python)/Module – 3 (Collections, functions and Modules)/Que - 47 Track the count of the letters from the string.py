'''
Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string. 
Sample string: 'w3resource' 
Expected output: 
{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''

# Sample string
sample_string = 'w3resource'

# Initialize an empty dictionary to store the letter counts
letter_count = {}

# Count occurrences of each letter in the string
for letter in sample_string:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

# Display the resulting dictionary
print(letter_count)
