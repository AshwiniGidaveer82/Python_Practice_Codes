def reverseString(s):
    left, right = 0, len(s) - 1  
    while left < right:
        s[left], s[right] = s[right], s[left]  
        left += 1
        right -= 1


s1 = ["h", "e", "l", "l", "o"]
reverseString(s1)
print(s1)  # Output: ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
reverseString(s2)
print(s2)  # Output: ["h", "a", "n", "n", "a", "H"]
