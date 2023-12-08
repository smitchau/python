#Write a Python program to unzip a list of tuples into individual lists. 

#create three list
l1 = [1,2,3,4,5]
l2 = ['smit','nikhil','tirth','jay']
l3 = [21,51,43,54]

#use zip function
zip1 = list(zip(l1,l2,l3))
print("original list of tuple :",zip1)

#again create empty three list 
lis1 = []
lis2 = []
lis3 = []

#unzip a list of tuples into individual lists

for i in zip1:
    lis1.append(i[0]) #individual list and unzip list of tuple
    lis2.append(i[1])
    lis3.append(i[2])

print("\nindividual list1 :",lis1)
print("individual list2 :",lis2)
print("individual list3 :",lis3)
