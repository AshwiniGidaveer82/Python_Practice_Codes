def countBits(n):
    return [bin(i).count('1') for i in range(n + 1)]


print(countBits(2))  # Output: [0, 1, 1]
print(countBits(5))  # Output: [0, 1, 1, 2, 1, 2] 
