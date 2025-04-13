def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [1,2,3,4,5]
print(singleNumber(nums))