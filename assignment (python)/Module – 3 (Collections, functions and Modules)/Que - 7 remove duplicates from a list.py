'''
Write a Python program to remove duplicates from a list.
'''

l1 = [2,4,6,8,9,5,3,2,4,1,8,9,6,3,2,4,6,10,1]

l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)

print("new list is : ",l2)
