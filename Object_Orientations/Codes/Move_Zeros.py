def moveZeroes(nums):
    non_zero_index = 0  

   
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

    return nums  

nums1 = [0,1,0,3,12]
moveZeroes(nums1)
print(nums1)  # Output: [1,3,12,0,0]

nums2 = [0]
moveZeroes(nums2)
print(nums2)  # Output: [0]
