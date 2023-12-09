# Write a Python program to returns sum of all divisors of a number 

# Input value
input_number = 5

divisor_sum = 0  # Initialize the sum of divisors

# Iterate from 1 to the number
for i in range(1, input_number + 1):
    if input_number % i == 0:  # Check if 'i' is a divisor of 'input_number'
        divisor_sum += i  # Add 'i' to the sum of divisors

# Display the result
print(f"The sum of divisors of {input_number} is: {divisor_sum}")
