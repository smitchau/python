l1 = [1,1,2,3,4,5,3,2,5,5,67,8,9,6,5]

unique_li = []

for i in l1:
    if i not in unique_li:
        unique_li.append(i) 
print(unique_li)
