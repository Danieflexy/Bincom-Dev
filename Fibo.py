
# Function to generate Fibonacci sequence up to n terms
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

# Sum of the first 50 Fibonacci numbers
sum_of_fibonacci = sum(generate_fibonacci(50))

print("Sum of the first 50 Fibonacci numbers:", sum_of_fibonacci)
