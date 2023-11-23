#Write a Python program to check whether a list contains a sub list 

list = [4,6,3,2,7,9,8,10,1,5]

sub_list = [7,9,5]

c = 0
res = False

for i in sub_list:
    if i in list:
        c += 1
        
if c == len(sub_list):
    res = True

print("sublist present in list ? : ",res)
