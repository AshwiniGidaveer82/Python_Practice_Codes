def my_isalpha(s):
    for char in s:
        if not ('A' <= char <= 'Z' or 'a' <= char <= 'z'):  
            return False
    return bool(s) 


print(my_isalpha("Hello"))      # True
print(my_isalpha("Hello123"))   # False

