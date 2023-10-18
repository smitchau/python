no = int(input("how many no you want to enter :"))
li1=[]
for i in range(0,no):
    li = int(input("Enter element : "))

    li1.append(li)
    
print("before shorting : ",li1)

for i in range(len(li1)):
    for j in range(i+1,len(li1)):

        if li1[i] < li1[j] :

            li1[i],li1[j] = li1[j],li1[i]

print("after shorting : ",li1)

