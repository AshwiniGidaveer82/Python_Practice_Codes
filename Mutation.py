def mutation(s, pos, char):
    li = list(s)
    li[pos] = char
    res = ''.join(li)
    return res

res = mutation('Kodnest',0,'A')
print(res)