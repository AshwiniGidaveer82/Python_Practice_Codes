def two_sum(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target: # type: ignore
                return [i, j]
            
nums = [1,2,3,5,6,7]
target = 9
print(two_sum(nums))