from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left)

        return max_len

nums = list(map(int, input("Enter binary numbers separated by space: ").split()))

sol = Solution()
result = sol.longestSubarray(nums)

print("Longest subarray of 1s after deleting one element:", result)
