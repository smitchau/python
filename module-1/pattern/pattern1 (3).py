"""


1 
1 0 
1 0 1 
1 0 1 0 
1 0 1 0 1

"""
for i in range(6):
    for j in range(i):
        if(j%2==1):
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
