def double(x):
    return (x*2)

li = [1,2,3,4]
new_li = list(map(double,li))
print(new_li)

tup = (10,20,30)
print(tup)
tup = tuple(map(int,tup))
print(tup)

li = [10,20,30]
print(li)
li= list()
print(li)