f = open('studentinfo.txt','w')

for i in range(1,3):
    iD = int(input("Enter id : "))
    name = input("Enter name : ")
    roll_no = int(input("Enter roll number : "))
    f.write(f"\nstudent info : {iD}{name}{roll_no}")
    
f.close()
