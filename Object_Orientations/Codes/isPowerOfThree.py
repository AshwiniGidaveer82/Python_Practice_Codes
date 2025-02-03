def isPowerOfThree(n: int) -> bool:
    if n <= 0:
        return False

    while n % 3 == 0:
        n //= 3 
    return n == 1  # If reduced to 1, it's a power of 3


test_numbers = [27, 0, -1, 9, 81, 10, 243]

for num in test_numbers:
    print(f"{num} is a power of three: {isPowerOfThree(num)}")
