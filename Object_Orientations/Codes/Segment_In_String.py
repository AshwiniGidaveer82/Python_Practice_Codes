def countSegments(s: str) -> int:
    count = 0
    in_segment = False

    for char in s:
        if char != ' ':  
            if not in_segment: 
                count += 1
                in_segment = True
        else:
            in_segment = False  
    return count

print(countSegments("Hello, my name is John"))  # Output: 5
print(countSegments("   "))  # Output: 0

