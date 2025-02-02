def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1

print(isPowerOfTwo(1))   # True
print(isPowerOfTwo(16))  # True
print(isPowerOfTwo(0))   # False
