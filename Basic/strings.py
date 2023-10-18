'''

    Strings in python : "collection of characters "

    blank string declaration : "hello",'hello'

    in-built class : str()

    Characteristics:

    they are indexible (starts with zero) 
    iterable
    
'''

str1 = "Hello World"


print(str1[0])
print(type(str1))
print("Lemngth of string : ",len(str1))

print(">>>>>>>Loop on string : ")
for character in str1:
    print(character)
