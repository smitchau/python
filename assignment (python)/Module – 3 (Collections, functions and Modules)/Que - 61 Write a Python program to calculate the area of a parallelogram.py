#Write a Python program to calculate the area of a parallelogram

def calculate_parallelogram_area(base, height):
    area = base * height  # Formula for the area of a parallelogram
    return area

# Input values (base, height)
base_value = 8  # Replace with the length of the base
height_value = 5  # Replace with the height of the parallelogram

# Calculate the area of the parallelogram
area = calculate_parallelogram_area(base_value, height_value)

# Display the result
print(f"The area of the parallelogram is: {area}")
