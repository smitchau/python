'''
 Write a Python program to calculate surface volume and area of a cylinder
'''

import math

# Input values (radius and height)
radius = 5  # Replace with the radius of the cylinder
height = 10  # Replace with the height of the cylinder

# Calculate the surface area of the cylinder
surface_area = 2 * math.pi * radius * (radius + height)

# Calculate the volume of the cylinder
volume = math.pi * radius ** 2 * height

# Calculate the lateral surface area of the cylinder
lateral_area = 2 * math.pi * radius * height

# Display the results
print(f"Surface Area of the Cylinder: {surface_area}")
print(f"Volume of the Cylinder: {volume}")
print(f"Lateral Area of the Cylinder: {lateral_area}")
