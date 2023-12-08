# How can you pick a random item from a range?

import random  # Importing the random module

# Take user input for the range
number_range = int(input("Enter range: "))

# Generate a random integer between 1 and the specified range (inclusive)
num = random.randint(1, number_range)

# Print the randomly chosen item from the range
print("Randomly chosen item from the range:", num)


'''
#second method

rang = range(100,200)

choice = random.choice(rang)

print("Randomly chosen item from the range: "choice)


'''
