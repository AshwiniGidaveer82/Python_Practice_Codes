class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]

if __name__ == "__main__":
    n = int(input())
    sol = Solution()
    print("Number of ways to tile the board:", sol.numTilings(n))
