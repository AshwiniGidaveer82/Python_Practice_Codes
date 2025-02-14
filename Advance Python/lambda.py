# li = [1,2,3,4]
# def even(ele):
#     return ele%2 == 0

# newli = list(filter(even,li))
# print(newli)
from functools import reduce
li = [1,2,3,4]
newli = list(filter(lambda num:num%2 == 0, li))
print(newli)

sum = reduce(lambda a,b: a+b, li)
print(sum)

square = list(map(lambda num: num**2, li))
print(square)


