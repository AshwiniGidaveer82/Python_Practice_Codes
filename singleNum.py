from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  
        return result
nums = [2, 3, 2, 4, 4]
print(nums)