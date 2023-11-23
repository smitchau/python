# Write a Python program to replace last value of tuples in a list

l1 = [(10,20,30),(40,50,60),(70,80,90)]

l2 = [i[:-1] + (100,) for i in l1]

print(l2)
