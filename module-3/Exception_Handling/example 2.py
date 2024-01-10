try:
    num1 = int(input("Enter number 1 :"))
    num2 = int(input("Enter numebr 2 :"))
    ans = num1/num2
    print(ans)

except ValueError:
    print("invalid input")

except ZeroDivisionError:
    print("cannot divided by zero")