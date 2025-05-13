def longestOnes(nums, k):
    left = 0
    max_len = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  
# Output: 6

print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  
# Output: 10
