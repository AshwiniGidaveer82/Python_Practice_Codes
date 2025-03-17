import math

def is_perfect_square(n):
    if n < 0:
        return False  
    
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n  


n = int(input("Enter a number: "))
if is_perfect_square(n):
    print(f"{n} is a perfect square.")
else:
    print(f"{n} is NOT a perfect square.")
