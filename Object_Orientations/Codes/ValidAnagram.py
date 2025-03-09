#  Using Counter 
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)


print(is_anagram("anagram", "nagaram"))  # Output: True
print(is_anagram("rat", "car"))          # Output: False

#  [2] Second Method

def is_anagram(s,t):
    return sorted(s) == sorted(t)

print(is_anagram("anagram", "naagram"))
