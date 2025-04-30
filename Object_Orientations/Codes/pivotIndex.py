def pivotIndex(nums):
    total = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        right_sum = total - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num

    return -1
print(pivotIndex([1, 7, 3, 6, 5, 6]))  # Output: 3
print(pivotIndex([1, 2, 3]))           # Output: -1
print(pivotIndex([2, 1, -1]))          # Output: 0
