#get unique values from a list

li1 = [11, 45, 32, 52, 58, 87, 76, 32, 54, 45, 96, 58, 11, 54, 96, 32]  # Given list of numbers

unique_values = []  # Empty list to store unique values

for i in li1:  # Iterate through each element in li1
    if i not in unique_values:  # Check if the element is not already in unique_values
        unique_values.append(i)  # If not, add the element to unique_values

print(unique_values)  # Print the list containing unique values from li1

