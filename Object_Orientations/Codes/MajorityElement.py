def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]  


print(majorityElement([3,2,3]))  # Output: 3
print(majorityElement([2,2,1,1,1,2,2]))  # Output: 2
