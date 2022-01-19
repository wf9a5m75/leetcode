class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        INF = 2**31 - 1
        dp = [[INF] * (M) for _ in range(N)]

        dp[0][0] = grid[0][0]
        for y in range(N):
            for x in range(M):
                if (y + 1 < N):
                    dp[y + 1][x] = min(dp[y + 1][x], dp[y][x] + grid[y + 1][x])
                if (x + 1 < M):
                    dp[y][x + 1] = min(dp[y][x + 1], dp[y][x] + grid[y][x + 1])
        return dp[N - 1][M - 1]
