#Write a Python program to find the highest 3 values in a dictionary

dic = {1: 34, 2: 42, 3: 13, 4: 63, 5: 94, 6: 12, 7: 21, 8: 57, 9: 41}

# Sort the values of the dictionary in ascending order and assign it to the variable dict
dict = sorted(dic.values())

# Print the last three elements (the three largest values) from the sorted list of values
print(dict[-3:])

