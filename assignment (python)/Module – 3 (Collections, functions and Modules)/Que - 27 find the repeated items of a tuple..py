# Write a Python program to find the repeated items of a tuple.

tup = (1, 22, 22, 55, 35, 55)  # Given tuple with some repeated elements

l1 = []  # Empty list to store unique elements
repeated_item = []  # Empty list to store repeated elements

for i in tup:  # Iterate through each element in the tuple
    if i not in l1:  # Check if the element is not already in the list of unique elements
        l1.append(i)  # If not, add the element to the list of unique elements
    else:
        repeated_item.append(i)  # If it's already in the list, add it to the list of repeated elements

print("repeated items of a tuple:", tuple(repeated_item))  # Print the repeated items as a tuple
