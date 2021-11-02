class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        M, N = len(grid), len(grid[0])

        INF = 2**31 - 1

        row = [INF] * (N + 1)
        dp = [row.copy() for _ in range(M + 1)]
        dp[0][0] = 0


        for y in range(M):
            for x in range(N):
                dp[y][x] += grid[y][x]

                dp[y + 1][x] = min(dp[y + 1][x], dp[y][x])
                dp[y][x + 1] = min(dp[y][x + 1], dp[y][x])

        return dp[M - 1][N- 1]
