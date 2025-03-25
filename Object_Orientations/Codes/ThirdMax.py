def thirdMax(nums):
    unique_nums = list(set(nums))
    unique_nums.sort(reverse=True)
    if len(unique_nums) >= 3:
        return unique_nums[2]
    else:
        return unique_nums[0]

print(thirdMax([3, 2, 1]))  # Output: 1
print(thirdMax([1, 2]))     # Output: 2
print(thirdMax([2, 2, 3, 1]))  # Output: 1
