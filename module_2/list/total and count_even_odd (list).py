
li1 = [1,2,3,4,5,6,7,8,9,10]

even_total = 0
odd_total = 0
count1 = 0
count2 = 0

for i in li1:
    if(i % 2 == 0):
        even_total = even_total + i
        count1 +=1
    else:
        odd_total = odd_total +i
        count2 +=1

print("Even total is :", even_total)
print("odd total is :",odd_total)
print("even no count :", count1)
print("odd no count :", count2)
    


