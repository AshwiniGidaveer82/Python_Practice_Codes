num = int(input())
product = 1
while num > 0:
    digit = num % 10
    product *= digit
    num //= 10
print(f"The product of all digits is {product}.")