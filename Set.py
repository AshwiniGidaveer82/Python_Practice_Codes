#  Set store homo and hetero type data
# Set is an unordered collection of data
#  Set is mutable
# Set cannot set repeat value
# 
set = {10,20,'Kodnest',True}
print(set, type(set))

s1 = {10,20,30}
s1.add(40)
print(s1)

s1.remove(40)
print(s1)

poped_ele = s1.pop()
print(poped_ele)
print(s1)