def isMonotonic(nums):
    increasing = decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            increasing = False
        if nums[i] > nums[i-1]:
            decreasing = False
    
    return increasing or decreasing


print(isMonotonic([1, 2, 2, 3]))  # Output: True
print(isMonotonic([6, 5, 4, 4]))  # Output: True
print(isMonotonic([1, 3, 2]))     # Output: False



# Second Method

def isMonotonic(nums):
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)


print(isMonotonic([1, 2, 2, 3]))  # Output: True
print(isMonotonic([6, 5, 4, 4]))  # Output: True
print(isMonotonic([1, 3, 2]))     # Output: False
