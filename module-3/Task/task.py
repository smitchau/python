li1 = ['smit','nikhil','purshottam','tirth']
li2 = ['python','java','php','wd']

'''
dic = dict(zip(li1,li2))

print(dic)


'''

dict = {}

for i in li1:
   for j in li2:
       dict[i] = j          
       li2.remove(j)
       break
print(dict)

