def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]

    return answer

print(productExceptSelf([1,2,3,4]))  # Output: [24,12,8,6]
print(productExceptSelf([-1,1,0,-3,3]))  # Output: [0,0,9,0,0]
