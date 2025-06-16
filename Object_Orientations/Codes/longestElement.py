from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

# Take input from user
nums = list(map(int, input().split()))
k = int(input())

# Call the function
sol = Solution()
result = sol.findKthLargest(nums, k)

print(f"The {k}th largest element is: {result}")
