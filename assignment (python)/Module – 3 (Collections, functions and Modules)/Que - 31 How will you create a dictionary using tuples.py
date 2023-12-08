#How will you create a dictionary using tuples in python?

# This code creates a dictionary where users input keys and corresponding tuples of values.
dict1 = {}
no = int(input("How many number of tuples to insert into the dictionary: "))
n1 = int(input("How many number of data to insert into each tuple: "))

for i in range(1, no + 1):
    lis = []
    key = input(f"\nEnter key {i}: ")
  
    for j in range(1, n1 + 1):
        value = input(f"Enter value {j}: ")
        lis.append(value)
        
    tup = tuple(lis)
    dict1.update({key: tup})

print("\nDictionary:", dict1)
# End of the code.
