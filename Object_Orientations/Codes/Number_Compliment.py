def findComplement(num):
    binary = bin(num)[2:]  
    complement = ''.join('0' if bit == '1' else '1' for bit in binary)  
    return int(complement, 2)  

print(findComplement(5))  # Output: 2
print(findComplement(1))  # Output: 0
