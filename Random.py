
import random

# Generate a random 4-digit binary number
binary_number = ''.join(random.choice('01') for _ in range(4))

# Convert binary number to base 10
decimal_number = int(binary_number, 2)

print("Generated binary number:", binary_number)
print("Converted to base 10:", decimal_number)
