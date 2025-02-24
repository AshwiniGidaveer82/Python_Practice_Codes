from collections import Counter

def firstUniqChar(s):
    count = Counter(s) 
    for i, char in enumerate(s):
        # for i in range(len(s)): // Less Readable
        if count[char] == 1:
            return i

    return -1  


print(firstUniqChar("leetcode"))      # Output: 0
print(firstUniqChar("loveleetcode"))  # Output: 2
print(firstUniqChar("aabb"))          # Output: -1
