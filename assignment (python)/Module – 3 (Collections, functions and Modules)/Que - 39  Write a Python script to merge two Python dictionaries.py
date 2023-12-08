# Write a Python script to merge two Python dictionaries 

dic1 = {'smit':1,'nik':2,'purshottam':3,'tirth':4}
dic2 = {'Gujarat':'Ghandhinagar','Rajashthan':'jaipur'}

for i in dic2:
    # Update dic1 with dic2
    dic1.update(dic2)

print(dic1)

'''
second method

li1 = list(dic1.items())
li2 = list(dic2.items())

for i in li2:
    li1.append(i)

print(dict(li1))
'''

