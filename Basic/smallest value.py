n1 = int(input("Enter value one : "))
n2 = int(input("Enter value two : "))
n3 = int(input("Enter value three : "))

if (n1<n2):
    if(n1<n3):
        print("n1 is small")
    else:
        print("n3 is small")
else:
    if(n2<n3):
        print("n2 is small")
    else:
        print("n3 is small")

