def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))  

print(solve("hello  world"))  # Output: "Hello  World" 
