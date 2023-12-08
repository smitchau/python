'''
list.append(x) :  Add an item to the end of the list.

list.extend(L) : Appends the contents of L to list
'''

list = ['python', 'java', 'c++', 'c', 'html']  # Creating a list
list2 = []  # Creating an empty list

print('before list: ', list)  # Printing the content of the 'list' before modification

list.append('smit')  # Appending 'smit' to the 'list'

print('after list using append: ', list)  # Printing the content of the 'list' after appending 'smit'

list2.extend(list)  # Extending 'list2' by adding all elements from 'list'

print('after list2 extend list: ', list2)  # Printing the content of 'list2'
