class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        INF = 1000000
        N = len(cost)
        dp = [INF] * (N + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(N):
            dp[i + 1] = min(dp[i + 1], dp[i] + cost[i])
            if (i + 2 <= N):
                dp[i + 2] = min(dp[i + 2], dp[i] + cost[i])

        return dp[N]
