def count_ones(n):
    return bin(n).count('1')

def sortByBits(arr):
    return sorted(arr, key=lambda x: (count_ones(x), x))

arr = [0,1,2,3,4,5,6,7,8]
print(sortByBits(arr))
