#import random module

import random

#create list

li = []
ul = []
cl = []
n=1

# users insert element in the list

for i in range(1,13):
    n1 = int(input(f"Enter number {n} : "))
    li.append(n1)
    n+=1
print("list : ",li)

# append element in user list and computer list

no=1
for i in li:
    if no%2 == 0:
         ul.append(i)
    else:
         cl.append(i)
    no += 1
         
print("\nuser list : ",ul)   
print("\ncomputer list : ",cl)

#random choice number in the list and remove element in list
counter_ul = 0
counter_cl = 0
u=1
c=1
for i in range(1,13):

    # random choice number
    r = random.choice(li)
     
    #remove element
    if r in ul:
        ul.remove(r)
        counter_ul += 1
        print(f"\nnew user list {u}: ",ul)
        print(f"new com list {c}: ",cl) 
    elif r in cl:
        cl.remove(r)
        counter_cl += 1
        print(f"\nnew user list {u}: ",ul)
        print(f"new com list {c}: ",cl)
        
    li.remove(r)
    u+=1
    c+=1

    #winner condition
    
    if counter_ul==6:
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<  user is win  >>>>>>>>>>>>>>>>>>>>>>>>>")
        break
    elif counter_cl==6:
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<  computer us win  >>>>>>>>>>>>>>>>>>>>>>>>>")
        break
        
        



