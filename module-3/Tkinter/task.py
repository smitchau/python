li1 = [1,2,3,4]
li2 = [32,34,56,77]
dic = {}

for i in range(len(li2)):
    if i < len(li1):
        dic[li1[i]] = li2[i]

print(dic)