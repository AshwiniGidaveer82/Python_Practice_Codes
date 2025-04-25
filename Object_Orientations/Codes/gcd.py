import math

def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    gcd_length = math.gcd(len(str1), len(str2))
    return str1[:gcd_length]
print(gcdOfStrings("ABCABC", "ABC"))    # Output: "ABC"
print(gcdOfStrings("LEET", "CODE"))     # Output: ""