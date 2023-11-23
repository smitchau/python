# Write a Python program to find the repeated items of a tuple.

tup = (1,22,22,55,35,55)

l1=[]

repeated_item = []


for i in tup:
    if i not in l1:
        l1.append(i)
    else:
        repeated_item.append(i)

print("repeated items of a tuple :",tuple(repeated_item))

