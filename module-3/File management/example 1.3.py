f = open('example 1.1.txt','r')

r = f.read()

s = r.split()   #word ko space se seprete karta hai use word count karne ke liye hota he

print(s)

#===========Exapmple===============
count = 0
for w in s:
    if not w.isnumeric():
        count+=1
        print(w)

print("total no of word are : ",count)
