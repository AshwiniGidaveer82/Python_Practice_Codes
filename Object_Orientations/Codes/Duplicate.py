def containsDuplicate(nums):
    return len(nums) != len(set(nums))  

print(containsDuplicate([1,2,3,1]))  # Output: True
print(containsDuplicate([1,2,3,4]))  # Output: False
