'''
Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary. 
Sample data: {'1': ['a','b'], '2': ['c','d']}

Expected Output: 
ac ad bc bd 
'''

dic = {1: ['a', 'b'], 2: ['c', 'd']}

# Outer loop iterating through elements of dic[1]
for i in dic[1]:
    # Inner loop iterating through elements of dic[2]
    for j in dic[2]:
        # Print the concatenation of elements i and j with a space as separator
        print(i + j, end=" ")

#use slicing
'''
dic1 = {'1': ['a','b'], '2': ['c','d']}

li = []
li1 = []

for values in dic1.values():
    li.append(values)

li1 = li[0][0] + li[1][0]
print(li1,end = " ")
li1 = li[0][0] + li[1][1]
print(li1,end = " ")
li1 = li[0][1] + li[1][0]
print(li1,end = " ")
li1 = li[0][1] + li[1][1]
print(li1,end = " ")
'''
