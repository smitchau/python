'''
Write a Python program to remove duplicates from a list.
'''

l1 = [2, 4, 6, 8, 9, 5, 3, 2, 4, 1, 8, 9, 6, 3, 2, 4, 6, 10, 1]  # Original list with duplicates

l2 = []  # Initializing an empty list

# Loop through each element in l1
for i in l1:
    if i not in l2:  # Check if the element is not already in l2
        l2.append(i)  # If not, add the element to l2

print("new list is:", l2)  # Print the new list without duplicates

