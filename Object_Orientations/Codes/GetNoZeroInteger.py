def getNoZeroIntegers(n):
    a = 1
    b = n - a
    while '0' in str(a) or '0' in str(b):
        a += 1
        b = n - a
    return [a, b]


print(getNoZeroIntegers(2))   # Output: [1, 1]
print(getNoZeroIntegers(11))  # Output: [2, 9] or [8, 3]
print(getNoZeroIntegers(101)) # Output: [12, 89] or other valid pairs
print(getNoZeroIntegers(19))  # Output: [1, 18] or [2, 17]
