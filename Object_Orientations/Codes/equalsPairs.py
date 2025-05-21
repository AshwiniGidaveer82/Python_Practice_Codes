from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        len(grid)
        count = 0

        columns = list(zip(*grid))

        for row in grid:
            for col in columns:
                if tuple(row) == col:
                    count += 1

        return count
sol = Solution()

grid1 = [[3,2,1],[1,7,6],[2,7,7]]
print(sol.equalPairs(grid1))  # Output: 1

grid2 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(sol.equalPairs(grid2))  # Output: 3
