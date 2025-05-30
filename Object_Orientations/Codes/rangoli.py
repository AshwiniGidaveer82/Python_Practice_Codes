def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []
    for i in range(size):
        left_part = '-'.join(alpha[size-1:i:-1])  
        right_part = '-'.join(alpha[i:size])      
        line = left_part + '-' + right_part if left_part else right_part
        line = line.center(4*size - 3, '-')      
        lines.append(line)

    print('\n'.join(lines[::-1] + lines[1:]))  

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
