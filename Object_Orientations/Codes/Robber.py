from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]            
        prev1 = max(nums[0], nums[1])  

        for i in range(2, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current

        return prev1



if __name__ == "__main__":
    nums = list(map(int, input().split()))
    sol = Solution()
    print("Maximum amount that can be robbed:", sol.rob(nums))
