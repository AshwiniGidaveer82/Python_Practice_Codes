def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):  
            primes.append(num)
    return primes


print(is_prime(7))      # Output: True
print(is_prime(10))     # Output: False
print(prime_numbers(20)) # Output: [2, 3, 5, 7, 11, 13, 17, 19]
