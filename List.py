"""
1. List can store homogeneous and heterogenious 
2. List can store Duplicate value
3. List are mutable

"""

list = [10,20,True,'Kodnest',20]
print(list, type(list))

list.append(300)
print(list)

list.insert(1,29)
print(list)

list.remove(300)
print(list)

list.remove(29)
print(list)

list.pop()
print(list)

li1=list.pop(10)
print(li1)
