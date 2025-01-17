li1 = [1,2,3,4,5]
print(li1)
sq_list = []
for i in li1:
    sq_list.append(i*i)
print(sq_list) 

duplicate_li1 = [i for i in li1]
print(duplicate_li1)
even = [i for i in li1 if i % 2 == 0]
print(even)
sq_li1 = [i*i for i in li1]
print(sq_li1)


lis1 = [1,2,3,4]
for i in lis1:
    if(i % 2 == 0):
        print("even")
    else: 
        print("odd")
print()