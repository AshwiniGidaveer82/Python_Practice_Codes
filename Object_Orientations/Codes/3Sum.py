def threeSum(nums):
    result = []
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in result:
                        result.append(triplet)
                        
    return result

print(threeSum([-1, 0, 1, 2, -1, -4]))

print(threeSum([0, 0, 0]))

print(threeSum([0, 1, 1]))

