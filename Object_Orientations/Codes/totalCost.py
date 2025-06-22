from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left, right = 0, n - 1
        total = 0

        left_heap = []
        right_heap = []

        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, (costs[left], left))
                left += 1
            if left <= right:
                heapq.heappush(right_heap, (costs[right], right))
                right -= 1

        for _ in range(k):
            if left_heap and (not right_heap or left_heap[0][0] <= right_heap[0][0]):
                cost, idx = heapq.heappop(left_heap)
                total += cost
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1
            else:
                cost, idx = heapq.heappop(right_heap)
                total += cost
                if left <= right:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1

        return total

# -----------------------------------
# 🧪 Input Handling & Test
# -----------------------------------
if __name__ == "__main__":
    # Example input: 17 12 10 2 7 2 11 20 8
    costs = list(map(int, input("Enter costs (space-separated): ").split()))
    k = int(input("Enter k (number of workers to hire): "))
    candidates = int(input("Enter number of candidates from each side: "))

    sol = Solution()
    result = sol.totalCost(costs, k, candidates)
    print("Minimum total cost to hire workers:", result)
