def removeAnagrams(words):
    result = []

    for word in words:
        if result and sorted(word) == sorted(result[-1]):
            continue 
        result.append(word)

    return result
print(removeAnagrams(["abba","baba","bbaa","cd","cd"]))  # Output: ["abba","cd"]
print(removeAnagrams(["a","b","c","d","e"]))             # Output: ["a","b","c","d","e"]
