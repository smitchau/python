def number(no):
    print(no)
    if no<=0:
        return 1
    else:
        return number(no-1)
    
number(10)
