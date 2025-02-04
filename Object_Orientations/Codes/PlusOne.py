def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9: 
            digits[i] += 1
            return digits
        digits[i] = 0  
    
  
    return [1] + digits

# Test cases
print(plusOne([1,2,3]))  # Output: [1,2,4]
print(plusOne([4,3,2,1]))  # Output: [4,3,2,2]