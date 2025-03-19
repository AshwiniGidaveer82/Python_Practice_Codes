def threeConsecutiveOdds(arr):
    for i in range(len(arr) - 2):
        if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
            return True
    return False

 
print(threeConsecutiveOdds([2, 6, 4, 1]))  # Output: False
print(threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))  # Output: True
