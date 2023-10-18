"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

"""
no=int(input("enter no :"))
n=1
for i in range(no):
    for j in range(i):
        print(n,end=" ")
        n=n+1
    print()
