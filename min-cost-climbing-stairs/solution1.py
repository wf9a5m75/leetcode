class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        INF = 1000000
        N = len(cost)
        def walker(start: int) -> int:
            dp = [INF] * (N + 1)
            dp[start] = 0
            for i in range(start, N):
                dp[i + 1] = min(dp[i + 1], dp[i] + cost[i])
                if (i + 2 <= N):
                    dp[i + 2] = min(dp[i + 2], dp[i] + cost[i])

            return dp[N]

        cost0 = walker(0)
        cost1 = walker(1)
        return min(cost0, cost1)
