#Write a Python program to convert degree to radian

import math

# Function to convert degrees to radians
def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)  # Formula to convert degrees to radians
    return radians

# Input degrees
degrees_value = 45  # Replace with the degree value you want to convert

# Convert degrees to radians
radians_value = degrees_to_radians(degrees_value)

# Display the result
print(f"{degrees_value} degrees is equal to {radians_value} radians.")
