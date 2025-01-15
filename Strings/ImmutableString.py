#  String doesnt chage the value
# s1 = "kodnest"
# s1 = s1.upper()
# print(s1)

# s1 = 'k'
# print(s1, id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1, id(s1))
print(s2, id(s2))
print(id(s1[-1]))
print(id(s1[0]))

print('s1 id of H', id(s1[0]))
print('s1 id of e', id(s1[1]))
print('s1 id of o', id(s1[-1]))

print('s2 id of W', id(s2[0]))
print('s2 id of o', id(s2[1]))
print('s2 id of l', id(s2[-2]))
