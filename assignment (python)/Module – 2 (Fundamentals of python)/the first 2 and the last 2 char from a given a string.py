'''
    Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string.
'''

str1 = input("Enter string : ")

if len(str1) <= 2:
    print("")
else:
    new = str1[0:2]+str1[-2:]

print("new formed string is : ",new)
