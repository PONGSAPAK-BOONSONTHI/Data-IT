"""Lab 05.01 - Summation V.1"""
def summation(n):
    if n == 1:
        return 1
    result = 0
    for i in range(n + 1):
        result += i
    return result
print(summation(int(input())))