class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

    
        for i in range(m + 1):
            dp[i][0] = i 
        for j in range(n + 1):
            dp[0][j] = j  
       
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  
                else:
                    insert_op = dp[i][j - 1]
                    delete_op = dp[i - 1][j]
                    replace_op = dp[i - 1][j - 1]
                    dp[i][j] = 1 + min(insert_op, delete_op, replace_op)

        return dp[m][n]
sol = Solution()
print(sol.minDistance("horse", "ros"))  # Output: 3
