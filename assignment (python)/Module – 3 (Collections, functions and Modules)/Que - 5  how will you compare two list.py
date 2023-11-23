li1 = [10,20,30,40,50]
li2 = [50,70,80,10,30]
li3 = [50,20,40,10,30]

list1 = sorted(li1)
list2 = sorted(li2)
list3 = sorted(li3)

if list1 == list2:
    print('list1 and list2 are same')
else:
    print('list1 and list2 are not same')

if list1 == list3:
    print('list1 and list3 are same')
else:
    print('list1 and list3 are not same')
