def maxNumberOfBalloons(text):
    text = text.lower()
    mp = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
    
    for char in text:
        if char in mp:
            mp[char] += 1

    return min(mp["b"], mp["a"], mp["l"] // 2, mp["o"] // 2, mp["n"])

# 🔍 Test cases
print(maxNumberOfBalloons("nlaebolko"))           # Output: 1
print(maxNumberOfBalloons("loonbalxballpoon"))    # Output: 2
print(maxNumberOfBalloons("leetcode"))            # Output: 0
