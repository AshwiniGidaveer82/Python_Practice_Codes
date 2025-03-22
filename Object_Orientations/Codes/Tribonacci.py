def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    t0, t1, t2 = 0, 1, 1
    for i in range(3, n + 1):
        tn = t0 + t1 + t2
        t0, t1, t2 = t1, t2, tn
    
    return tn


print(tribonacci(4))   # Output: 4
print(tribonacci(25))  # Output: 1389537
