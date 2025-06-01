def merge_the_tool(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        seen = ""
        for char in substring:
            if char not in seen:
                seen += char
        print(seen)
string, k = input(), int(input())
print(merge_the_tool(string, k))