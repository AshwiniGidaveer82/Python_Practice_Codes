def arrayPairSum(nums):
    nums.sort() 
    return sum(nums[::2])  

print(arrayPairSum([1,4,3,2]))  # Output: 4
print(arrayPairSum([6,2,6,5,1,2]))  # Output: 9
