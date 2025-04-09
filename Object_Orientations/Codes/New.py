def countFullyTypedWords(text: str, brokenLetters: str) -> int:
    words = text.split()  
    broken_set = set(brokenLetters) 
    return sum(all(ch not in broken_set for ch in word) for word in words)  
 
print(countFullyTypedWords("hello world", "ad"))  # Output: 1
print(countFullyTypedWords("leet code", "lt"))   # Output: 1
print(countFullyTypedWords("leet code", "e"))    # Output: 0
