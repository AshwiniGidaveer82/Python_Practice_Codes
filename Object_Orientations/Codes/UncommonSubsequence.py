def findLUSlength(a, b):
    if a == b:
        return -1
    return max(len(a), len(b))


print(findLUSlength("aba", "cdc"))  # Output: 3
print(findLUSlength("aaa", "aaa"))  # Output: -1
