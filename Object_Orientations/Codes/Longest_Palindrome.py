from collections import Counter

def longestPalindrome(s: str) -> int:
    char_counts = Counter(s)
    length = 0
    has_odd = False
    
    for count in char_counts.values():
        length += count // 2 * 2  
        if count % 2 == 1:
            has_odd = True  
    return length + 1 if has_odd else length


print(longestPalindrome("abccccdd"))  # Output: 7
print(longestPalindrome("a"))         # Output: 1
