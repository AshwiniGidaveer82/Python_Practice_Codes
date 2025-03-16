def decimal_to_binary(n):
    return bin(n)[2:]  

num = int(input("Enter a decimal number: "))
print(f"Binary: {decimal_to_binary(num)}")
