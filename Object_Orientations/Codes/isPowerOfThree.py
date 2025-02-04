def isPowerOfThree(n: int) -> bool:
    if n <= 0:
        return False

    while n % 3 == 0:
        n //= 3 
    return n == 1  


test_numbers = [27, 0, -1, 9, 81, 10, 243]

for num in test_numbers:
    print(f"{num} is a power of three: {isPowerOfThree(num)}")
