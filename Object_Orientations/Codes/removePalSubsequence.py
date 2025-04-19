def removePal(s):
    if s == s[::-1]:
        return 1
    return 2

print(removePal("ababa"))
print(removePal("abb"))