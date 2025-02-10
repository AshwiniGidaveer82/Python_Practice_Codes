import re

def isPalindrome(s: str) -> bool:

    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    return cleaned_s == cleaned_s[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(isPalindrome("race a car"))  # Output: False
print(isPalindrome(" "))  # Output: True
