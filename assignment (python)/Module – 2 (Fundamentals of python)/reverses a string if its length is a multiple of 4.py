'''
 Write a Python function to reverses a string if its length is a multiple of 4.
'''


str=input("Enter the String :")

if len(str) % 4 == 0:
   print(''.join(reversed(str)))
else:
    print(str)

'''
str.join(iterable)

 Return a string which is the concatenation of the strings in the iterable. 
A TypeError will be raised if there are any non-string values initerable, 
including bytes objects. The separator between elements is the string 
providing this method.
'''
