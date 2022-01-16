class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        INF = 2**31 - 1
        dp = [[INF] * N for _ in range(N + 1)]
        dp[0] = matrix[0]

        for y in range(N - 1):
            for x in range(N):
                if (x - 1 >= 0):
                    dp[y + 1][x - 1] = min(dp[y + 1][x - 1], dp[y][x] + matrix[y + 1][x - 1])

                dp[y + 1][x] = min(dp[y + 1][x], dp[y][x] + matrix[y + 1][x])

                if (x + 1 < N):
                    dp[y + 1][x + 1] = min(dp[y + 1][x + 1], dp[y][x] + matrix[y + 1][x + 1])
        return min(dp[N - 1])
