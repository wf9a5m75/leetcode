class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        INF = float("inf")
        dp = [[INF] * (N + 1) for _ in range(N + 1)]

        dp[0][0] = 0
        for i in range(N):
            for j in range(i + 1):
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + triangle[i][j])
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + triangle[i][j])
        return min(dp[N])
