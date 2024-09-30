def fibonacci(n):
    fib_sequence = [0, 1]  # Starting the sequence with 0 and 1
    
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Number of Fibonacci numbers to print
n = 10

# Print the first ten Fibonacci numbers
fib_numbers = fibonacci(n)
print(fib_numbers)
    
