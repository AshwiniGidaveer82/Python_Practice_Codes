def mejority(nums):
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num
        
nums = [3,3,4,2,3,3]
print("Mejority Element is:",mejority(nums))