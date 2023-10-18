#Write a Python program to count the number of characters (character frequency) in a strin


str = 'Good Morning'
count = {}
for i in str:
    if i in count:
        count[i]+= 1
    else:
        count[i]=1
print("The number of character",count)
