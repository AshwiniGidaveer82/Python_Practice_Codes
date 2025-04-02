def countBinarySubstrings(s):
    groups = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count) 
   
    result = 0
    for i in range(1, len(groups)):
        result += min(groups[i], groups[i - 1])

    return result

s1 = "00110011"
s2 = "10101"
print(countBinarySubstrings(s1))  # Output: 6
print(countBinarySubstrings(s2))  # Output: 4
