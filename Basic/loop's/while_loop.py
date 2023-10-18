'''
while loop :

    Entry control loop
    most used for game application

    when we are not exact about number of iterations

    Syntax :

    initialization
    while condition:
        codee/...

'''
status=True
while status:
    print("Hello")

    choice=input("Do you want to continue? : ['y/n'] : ")
    if choice=='y':
        status=True
    else:
        status=False
