def isIsomorphic(s: str, t: str) -> bool:
    map1 = []
    map2 = []
    
    for idx in s:
        map1.append(s.index(idx))  # Store the first occurrence index of each character
    
    for idx in t:
        map2.append(t.index(idx))  # Store the first occurrence index of each character
    
    return map1 == map2  # Compare both lists

print(isIsomorphic("egg", "add"))   # Output: True
print(isIsomorphic("foo", "bar"))   # Output: False

