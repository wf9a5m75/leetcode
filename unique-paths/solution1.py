class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # The number of way to stand at the start location is only 1
        dp[0][0] = 1

        for y in range(n):
            for x in range(m):
                dp[y + 1][x] += dp[y][x]
                dp[y][x + 1] += dp[y][x]
        return dp[n-1][m-1]
