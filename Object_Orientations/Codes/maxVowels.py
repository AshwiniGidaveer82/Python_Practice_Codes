def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_count = count = 0

    # Initial window
    for i in range(k):
        if s[i] in vowels:
            count += 1
    max_count = count

    # Slide the window
    for i in range(k, len(s)):
        if s[i] in vowels:
            count += 1
        if s[i - k] in vowels:
            count -= 1
        max_count = max(max_count, count)

    return max_count
print(maxVowels("abciiidef", 3))  # Output: 3
print(maxVowels("aeiou", 2))      # Output: 2
print(maxVowels("leetcode", 3))   # Output: 2
