rows = 5

col = 5

for i in range(rows):

    for j in range(col):

        print('*',end=' ')

    print()

 

print()

for i in range(rows):

    for j in range(i+1):

        print('*',end=' ')

    print()

print()

for i in range(rows):

    for j in range(i, rows):

        print('*',end=' ')

    print()

 

for i in range(rows):

    for j in range(i+1):

        print('*',end=' ')

    print()

for i in range(rows):

    for j in range(i, rows-1):

        print('*',end=' ')

    print()

print()

for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    for j in range(i, rows-1):
        print(' ',end="")
    for j in range(i, rows-1):
        print(' ',end="")
    for j in range(i+1):
        print("*", end="")
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print("*", end="")
    for j in range(i+1):
        print(' ',end="")
    for j in range(i+1):
        print(' ',end="")
    for j in range(i,rows-1):
        print("*", end="")
    print()


print()
for i in range(rows):
    for j in range(i, rows-1):
        print(' ',end="")
    for j in range(i):
        print("*", end="")
    for j in range(i+1):
        print("*", end="")
    for j in range(i, rows-1):
        print(' ',end="")
    print()

for i in range(rows):
    for j in range(i+1):
        print(" ", end="")
    for j in range(i, rows-1):
        print('*',end="")
    for j in range(i, rows-2):
        print('*',end="")
    for j in range(i+1):
        print(" ", end="")
   
    print()


