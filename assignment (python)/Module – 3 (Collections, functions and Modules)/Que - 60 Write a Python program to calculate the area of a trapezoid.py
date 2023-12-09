#Write a Python program to calculate the area of a trapezoid

# Function to calculate the area of a trapezoid
def calculate_trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height  # Formula for the area of a trapezoid
    return area

# Input values (base1, base2, height)
base1_value = 3  # Replace with the length of the first base
base2_value = 4  # Replace with the length of the second base
height_value = 5  # Replace with the height of the trapezoid

# Calculate the area of the trapezoid
area = calculate_trapezoid_area(base1_value, base2_value, height_value)

# Display the result
print(f"The area of the trapezoid is: {area}")
