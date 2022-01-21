class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        if N < 3:
            return min(cost)

        INF = 2**31-1
        dp = [INF] * (N + 2)

        # Since we can start from 0 or 1,
        # to reach at 0 and 1 are zero.
        dp[0] = 0
        dp[1] = 0

        for i in range(N):
            dp[i + 1] = min(dp[i + 1], dp[i] + cost[i])
            dp[i + 2] = min(dp[i + 2], dp[i] + cost[i])
        return min(dp[N], dp[N + 1])
