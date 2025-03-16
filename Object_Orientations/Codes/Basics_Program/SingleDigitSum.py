def single_digit_sum(n):
    while n >= 10: 
        n = sum(int(digit) for digit in str(n))  
    return n


num = int(input("Enter a number: "))
print(f"Single-digit sum: {single_digit_sum(num)}")
