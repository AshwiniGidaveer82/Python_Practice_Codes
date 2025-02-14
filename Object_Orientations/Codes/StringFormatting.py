def print_formatted(num):
    width = len(bin(num)) - 2
    for i in range(1, num+1):
        dec = str(num).rjust(width)
        ot = oct(num)[2:].rjust(width)
        hx = hex(num).upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(f'{dec} {ot} {hx} {binary}')