from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
nums = list(map(int, input().split()))

# Call the function
sol = Solution()
peak_index = sol.findPeakElement(nums)

print(f"Peak element index: {peak_index}")
print(f"Peak element value: {nums[peak_index]}")
