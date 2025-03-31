def is_valid(s):
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    stack = []
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

print(is_valid("()"))       # Output: True
print(is_valid("()[]{}"))   # Output: True
print(is_valid("(]"))       # Output: False
print(is_valid("([])"))     # Output: True
