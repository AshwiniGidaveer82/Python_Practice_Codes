def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))  

print(solve("hello  world"))  # Output: "Hello  World" 


# Second Method 

def solve(s):
    if len(s) == 0:
        return s
    return s[0].upper() + s[1:].lower()

print(solve("python"))
