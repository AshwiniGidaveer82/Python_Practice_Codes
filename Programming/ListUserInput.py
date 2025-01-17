li = input('Enter space seperated by list')
print(li, type(li))
li = li.split()
print(li)
li = list(map(int, li))
print(li)

tup = tuple(map(int,input('Enter a number: ').split()))
print(tup)

li = list(map(int, input('Enter a number:').split()))
even_list = []
for i in range(li):
    if i % 2 == 0:
     print(i + " ")
