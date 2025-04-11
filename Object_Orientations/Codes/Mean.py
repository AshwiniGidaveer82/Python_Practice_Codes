def trimMean(arr):
    arr.sort()
    n = len(arr)
    remove_count = int(n * 0.05)
    trimmed = arr[remove_count : n - remove_count]
    return sum(trimmed) / len(trimmed)


arr1 = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
print(trimMean(arr1))  # Output: 2.0

arr2 = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
print(trimMean(arr2))  # Output: 4.0
