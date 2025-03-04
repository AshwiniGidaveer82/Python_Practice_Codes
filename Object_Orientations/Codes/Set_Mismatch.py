def findErrorNums(nums):
    seen = set()
    duplicate = -1
    
    for num in nums:
        if num in seen:
            duplicate = num
        seen.add(num)
    
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    missing = expected_sum - (actual_sum - duplicate)
    
    return [duplicate, missing]

print(findErrorNums([1,2,2,4]))  # Output: [2, 3]
print(findErrorNums([1,1]))      # Output: [1, 2]
