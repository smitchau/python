'''
Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings
'''

l1 = ['abc','bab','xyz','1001','c2c']
count = 0
for word in l1:
    if len(l1) > 2 and word[0] == word[-1]:
        count +=1
    else:
        count

print("same first and last character string is : ",count)
