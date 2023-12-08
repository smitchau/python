# Write a Python program to print all unique values in a dictionary.

d1 = {1: 23, 2: 43, 3: 23, 4: 44, 5: 54, 6: 23, 7: 44, 8: 54, 9: 43, 10: 54}
unique_value = set()  # Initialize an empty set to store unique values

# Iterate through the values in the dictionary d1
for value in d1.values():
    unique_value.add(value)  # Add each value to the unique_value set

print(unique_value)  # Print the set containing unique values

