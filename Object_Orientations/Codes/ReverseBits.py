def reverseBits(n: int) -> int:
    result = 0
    for i in range(32):  
        result = (result << 1) | (n & 1)  
        n >>= 1 
    return result


n = 0b00000010100101000001111010011100  
reversed_num = reverseBits(n)


print(reversed_num)  # output: 964176192
print(f"{reversed_num:032b}")  # output: 00111001011110000010100101000000
