d1={}
ds={}

no=int(input("How many students you want : "))

for i in range(no+1):
    name=input("Enter name : ")
    age=int(input("Enter age : "))
    sub=input("Enter subject : ")
    d1.update({age:sub})

    ds[name]=d1


print(ds)


