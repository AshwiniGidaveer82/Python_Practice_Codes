# string to integer conversion is not allowed

a = '30'
print(a,type(a))

x = 'KOD'
print(x, type(x))

# Float
p = float(input("Enter float type data"))
print(p, type(p))

# Boolean() BOOLEAN WILL NOT CONVERT THE INTEGER TO BOOLEAN AND BUT STRING WILL CONVERTED...
q = 'KOD'
print(q, type(q))
q = bool(q)
print(q, type(q))

value = int(float(input("price:", float )))