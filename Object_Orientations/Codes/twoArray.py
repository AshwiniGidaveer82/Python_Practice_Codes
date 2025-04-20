def findTheDistanceValue(arr1, arr2, d):
    count = 0
    for a in arr1:
        if all(abs(a - b) > d for b in arr2):
            count += 1
    return count
print(findTheDistanceValue([4,5,8], [10,9,1,8], 2)) 