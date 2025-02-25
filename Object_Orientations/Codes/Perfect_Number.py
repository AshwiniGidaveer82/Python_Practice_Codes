def is_perfect_number(num):
    if num <= 1:
        return False
    
    sum_divisors = sum(i for i in range(1, num // 2 + 1) if num % i == 0)
    
    return sum_divisors == num


print(is_perfect_number(28))  # Output: True
print(is_perfect_number(7))   # Output: False
