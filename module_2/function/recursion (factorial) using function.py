def number(fact):
    
    if fact<=0:
        return 1
    else:
        return fact*(fact-1)
    
print("factorial is :",number(5))
