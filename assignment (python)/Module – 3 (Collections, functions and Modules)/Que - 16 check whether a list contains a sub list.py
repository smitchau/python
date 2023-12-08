#Write a Python program to check whether a list contains a sub list 

list = [4, 6, 3, 2, 7, 9, 8, 10, 1, 5]  # Original list of numbers
sub_list = [8, 6, 4]  # Sublist to be checked

c = 0  # Counter to keep track of matches
res = False  # Initialize res as False

for i in sub_list:  # Loop through each element in the sub_list
    if i in list:  # Check if the element is present in the original list
        c += 1  # Increment the counter if the element is found

if c == len(sub_list):  # Check if the counter matches the length of the sub_list
    res = True  # If all elements in the sub_list are found in the original list, set res to True

print("sublist present in list? :", res)  # Print whether the sublist is present in the list
