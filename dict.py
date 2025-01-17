#  dict cant store duplicate key
#  dict can store duplicate value
#  
d1 = {'Name':'Ashu', 'age': 32, 'phone': 425363}
print(d1, type(d1))

d1['Name'] = 'Kavya'
print(d1)

for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i in d1.items():
    print(i)
