def repeatedSubstringPattern(s):
    return s in (s + s)[1:-1]

print(repeatedSubstringPattern("abab"))       # Output: True
print(repeatedSubstringPattern("aba"))        # Output: False

