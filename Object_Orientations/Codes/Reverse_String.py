def reverseStr(s: str, k: int) -> str:
    s = list(s) 
    
    for i in range(0, len(s), 2 * k):  
        s[i:i + k] = reversed(s[i:i + k])  

    return "".join(s) 

print(reverseStr("abcdefg", 2))  # Output: "bacdfeg"
print(reverseStr("abcd", 2))     # Output: "bacd"
