from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)

        min_heap = []
        sum1 = 0
        max_score = 0

        for i in range(len(pairs)):
            num2, num1 = pairs[i]
            heapq.heappush(min_heap, num1)
            sum1 += num1

            if len(min_heap) > k:
                sum1 -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                max_score = max(max_score, sum1 * num2)

        return max_score


nums1 = list(map(int, input("Enter nums1 elements separated by space: ").split()))
nums2 = list(map(int, input("Enter nums2 elements separated by space: ").split()))
k = int(input("Enter the value of k: "))


sol = Solution()
result = sol.maxScore(nums1, nums2, k)

print(f"Maximum score: {result}")
