class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP table filled with 1s
        dp = [[1] * n for _ in range(m)]
        
        # Start from cell (1,1) because first row and column are already 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]
    
m = int(input())
n = int(input())

sol = Solution()
print("Unique Paths:", sol.uniquePaths(m, n))
