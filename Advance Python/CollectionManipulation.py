li = [1,2,3,4]

def double(num):
    return num * 2

double_li = list(map(double, li))
print(double_li)

#Filter 

def checkEven(num):
    return num % 2 == 0

even_li = list(filter(checkEven, li))
print(even_li)

#Reduce

from functools import reduce
def mul(a,b):
    return a * b

res = reduce(mul, li)
print("Multiplication is: ", res)