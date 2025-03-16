import math

def find_gcd(a, b):
    return math.gcd(a, b)  

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"GCD of {num1} and {num2} is: {find_gcd(num1, num2)}")
