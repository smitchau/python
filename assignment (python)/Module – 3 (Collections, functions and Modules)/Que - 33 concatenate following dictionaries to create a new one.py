'''
Write a Python script to concatenate following dictionaries to create a 
new one.  '''

dic1 = {1:'python',2:'java',3:'c++'}      #create dictionaries
dic2 = {4:'html',5:'css',6:'javascript'}
dic3 = {7:'nodejs',8:'database'}

dic4 = {}

for i in (dic1,dic2,dic3):
    dic4.update(i)          # dictionaries are concate in dict4

print(dic4)
