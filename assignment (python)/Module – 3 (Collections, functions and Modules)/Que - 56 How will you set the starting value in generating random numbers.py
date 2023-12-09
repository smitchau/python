# How will you set the starting value in generating random numbers? 

import random

# Set the seed value (starting point)
random.seed(42)  # You can use any integer value as the seed

# Generate random numbers
rand_num1 = random.random()  # Example of generating a random floating-point number
rand_num2 = random.randint(1, 10)  # Example of generating a random integer between 1 and 10

print("Random number 1:", rand_num1)
print("Random number 2:", rand_num2)

