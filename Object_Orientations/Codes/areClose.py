from collections import Counter

def areClose(word1, word2):
    if set(word1) != set(word2):
        return False

    freq1 = sorted(Counter(word1).values())
    freq2 = sorted(Counter(word2).values())

    return freq1 == freq2


print(areClose("abc", "bca"))        # True
print(areClose("a", "aa"))           # False
print(areClose("cabbba", "abbccc"))  # True
