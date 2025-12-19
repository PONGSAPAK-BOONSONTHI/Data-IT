"""Lab 01.04 - Recursive GCD"""
def gcd(a, b):
    """Lab 01.04 - Recursive GCD"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = int(input())
b = int(input())
print(gcd(a, b))
