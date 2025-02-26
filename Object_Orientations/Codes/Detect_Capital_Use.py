def detectCapitalUse(word: str) -> bool:
    return word.isupper() or word.islower() or word.istitle()

print(detectCapitalUse("USA"))      # True
print(detectCapitalUse("FlaG"))     # False
print(detectCapitalUse("leetcode")) # True
print(detectCapitalUse("Google"))   # True
