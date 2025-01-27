s = 'Kodnest1234*'
print(s.isalnum())

s = 'Kodnest'
print(s.isalpha())

print('12'.isdigit())

print('apple'.islower())
print('apple'.isupper())

print(any((True, False, False)))
print(any((False, False, False)))

#---------------------------------------------#


s = input()
print(any([i.isalnum() for i in s]))
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))