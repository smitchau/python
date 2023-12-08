#Write a Python script to sort (ascending and descending) a dictionary by value. 

my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grapes': 3}

# Sorting dictionary by values in ascending order
ascending_sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

print("Dictionary sorted by value in ascending order (without lambda or operator):")
print(ascending_sorted_dict)

# Sorting dictionary by values in descending order without lambda or operator
descending_sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

print("Dictionary sorted by value in descending order (without lambda or operator):")
print(descending_sorted_dict)
