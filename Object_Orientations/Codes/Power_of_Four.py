def isPowerOfFour(n):
    return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0


print(isPowerOfFour(16))  # Output: True
print(isPowerOfFour(5))   # Output: False

