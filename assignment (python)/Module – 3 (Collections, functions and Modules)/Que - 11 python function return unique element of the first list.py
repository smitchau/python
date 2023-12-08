''' Write a Python function that takes a list and returns a new list with unique 
elements of the first list. '''

def unique():
    # Original list with duplicate elements
    li = [1, 1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7, 5, 8]

    unique_list = []  # Initializing an empty list to store unique elements

    # Iterating through each element in the original list
    for i in li:
        if i not in unique_list:  # Checking if the element is not already in the unique_list
            unique_list.append(i)  # If not, adding the element to the unique_list

    print('new list:', unique_list)  # Printing the list containing unique elements

unique()  # Calling the function
