def canBeTypedWords(text, brokenLetters):
    broken = set(brokenLetters)
    count = 0
    
    for word in text.split():
        if not any(char in broken for char in word):
            count += 1
    return count

print(canBeTypedWords("hello world", "ad"))   # Output: 1
print(canBeTypedWords("leet code", "lt"))     # Output: 1
print(canBeTypedWords("leet code", "e"))      # Output: 0
