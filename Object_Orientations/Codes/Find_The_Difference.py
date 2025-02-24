def findTheDifference(s: str, t: str) -> str:
    result = 0
    for char in s + t:
        result ^= ord(char)  
    return chr(result)


print(findTheDifference("abcd", "abcde"))  # Output: "e"
print(findTheDifference("", "y"))         # Output: "y"
