#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return

    # Special cases for small lengths
    if length == 1:
        print([0])
        return
    elif length == 2:
        print([0, 1])
        return

    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to the required length
    while len(fib_sequence) < length:
        # Append the next Fibonacci number
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    # Print the result
    print(fib_sequence)

# Example usage
print_fibonacci(0)  # Should print []
print_fibonacci(1)  # Should print [0]
print_fibonacci(2)  # Should print [0, 1]
print_fibonacci(10) # Should print [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

