li1 = [11,45,32,52,58,87,76,32,54,45,96,58,11,54,96,32]

unique_values = []

for i in li1:
    if i not in unique_values:
        unique_values.append(i)
        
print(unique_values)
