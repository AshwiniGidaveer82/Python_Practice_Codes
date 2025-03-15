def duplicateZeros(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == 0:
            arr.insert(i, 0)  
            arr.pop()  
            i += 1  
        i += 1


arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(arr1)
print(arr1)  # Output: [1, 0, 0, 2, 3, 0, 0, 4]