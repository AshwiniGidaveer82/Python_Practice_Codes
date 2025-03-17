def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial(n)}")
