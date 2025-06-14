from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # Step 1: Initialize queue with rotten oranges, count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes_passed = 0

        while queue:
            r, c, minutes = queue.popleft()
            minutes_passed = max(minutes_passed, minutes)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, minutes + 1))

        return minutes_passed if fresh == 0 else -1


if __name__ == "__main__":
    print("Enter the number of rows and columns (e.g., 3 3):")
    rows, cols = map(int, input().split())

    print("Enter the grid row by row:")
    grid = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)

  
    sol = Solution()
    result = sol.orangesRotting(grid)
    print("Output:", result)
