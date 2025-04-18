def max_69(num):
    max_list = list(str(num))
    for i in range(len(max_list)):
        if max_list[i] == '6':
            max_list[i] = '9'
            break
    return int("".join(max_list))

num = int(input())
print(max_69(num))