def myPow(x, n):
    if n == 0:
        return 1  
    
    if n < 0:
        x = 1 / x  
        n = -n

    result = 1
    while n > 0:
        if n % 2 == 1:  
            result *= x
        x *= x  
        n //= 2  

    return result


print(myPow(2.00000, 10))  # Output: 1024.00000s
print(myPow(2.00000, -2))  # Output: 0.25000
