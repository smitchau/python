# Write a Python program to read a random line from a file.

import random

file_name = 'emp_details.txt'  # Replace 'sample_file.txt' with your file name/path

try:
    # Attempt to open the file
    with open(file_name, 'r') as file:
        # Read all lines from the file into a list
        lines = file.readlines()
        
        # Choose a random line from the list of lines
        random_line = random.choice(lines)
        
        # Display the randomly chosen line after stripping any leading/trailing whitespace
        print("Random line from the file:")
        print(random_line.strip())
        
except FileNotFoundError:
    print("File not found. Please provide a valid file name or path.")

