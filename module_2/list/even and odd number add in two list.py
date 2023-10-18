li1 = []
li2 = []

no = int(input("Enter no : "))
for no in range(1,11):
    if no%2 == 0:
        li1.append(no)
    else:
        li2.append(no)

print("list1 :",li1)
print("list2 :",li2)
