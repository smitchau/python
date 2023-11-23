# Write a Python program to remove an empty tuple(s) from a list of tuples. 

lis1 = [(1,2,3),(4,5,6),(),(10,11),()]

for i in lis1:
    if i == tuple():
        lis1.remove(i)
    
print(lis1)


