file = open('example 1.1.txt','a')

for i in range(1,6):
    name = input("Enter your name : ")
    file.write("\n"+name)

file.close()