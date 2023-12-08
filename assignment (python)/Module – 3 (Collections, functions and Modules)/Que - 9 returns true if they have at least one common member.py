'''
 Write a Python function that takes two lists and returns true if they have 
at least one common member.
'''
def lists(l1, l2):
    result = False  # Initialize result as False
    
    # Nested loops to compare elements in l1 with elements in l2
    for i in l1:
        for j in l2:
            if i == j:  # If there's a match between elements
                result = True  # Update result to True
                return result  # Return result immediately upon finding a match

l1 = [1, 2, 3, 4, 5]  # First list
l2 = [5, 7, 6, 7, 8]  # Second list

print(lists(l1, l2))  # Call the function lists() and print the result

