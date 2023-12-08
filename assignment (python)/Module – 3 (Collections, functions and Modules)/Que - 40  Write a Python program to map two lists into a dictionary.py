# Write a Python program to map two lists into a dictionary 

# Define a function double that returns a tuple of its arguments
def double(x, y):
    return x, y

# Two lists with different types of elements
li1 = [1, 2, 3, 4, 5]
li2 = ['smit', 'purshottam', 'nik', 'tirth', 'raj']

# Using map() with double() function on li1 and li2
# This will create an iterable of tuples (x, y), where x is from li1 and y is from li2
mapped_values = map(double, li1, li2)

# Convert the iterable of tuples into a dictionary
result_dict = dict(mapped_values)

# Print the resulting dictionary
print(result_dict)

