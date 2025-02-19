def convertToTitle(columnNumber: int) -> str:
    result = []
    
    while columnNumber > 0:
        columnNumber -= 1  # Convert to 0-based index
        char = chr(columnNumber % 26 + ord('A')) 
        result.append(char)
        columnNumber //= 26  
    
    return ''.join(result[::-1])  


print(convertToTitle(1))    # Output: "A"
print(convertToTitle(28))   # Output: "AB"
print(convertToTitle(701))  # Output: "ZY"
