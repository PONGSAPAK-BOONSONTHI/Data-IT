"""Lab 01.05 - Fibonacci Number"""
def fibonacci(n):
    """Lab 01.05 - Fibonacci Number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(int(input())))
