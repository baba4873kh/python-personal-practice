def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]  # base cases
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

# Example usage:
n = int(input("Enter how many terms of Fibonacci you want: "))
series = fibonacci_series(n)
print("Fibonacci series up to", n, "terms:")
print(series)

