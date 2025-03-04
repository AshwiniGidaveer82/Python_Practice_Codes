def is_palindrome(s):
    return s == s[::-1]
s = "madam"
print(is_palindrome(s))