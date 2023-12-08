# Write a Python program to replace last value of tuples in a list
l1 = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]  # Given list of tuples

l2 = []  # Initializing an empty list

for tup in l1:  # Iterating through each tuple in l1
    ntup = tup[:-1] + (100,)  # Creating a new tuple by removing the last element and adding 100
    l2.append(ntup)  # Appending the new tuple to the list l2

print(l2)  # Printing the list l2 containing modified tuples

