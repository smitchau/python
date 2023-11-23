# WAP TO TAKE BLANK DICT AND TAKE USER INPUT AS NAME AGE AND SUBJECT AND POPOLATE THE DICT

d1 = {}

d2 = {}

for i in range(2):
    key = input("\nEnter key : ")
    for i in range(2):
        key1 = input("Enter nested key : ")
        value = input("Enter value : ")
        d2.update({key1:value})
        
    d1[key] = d2

print("\nprint nested dict: \n",d1)
