class Solution:
    def minCostClimbingStairs_backtrack(self, cost: List[int]) -> int:

        N = len(cost)

        @cache
        def dp(i : int) -> int:
            if i >= N:
                return 0
            return min(dp(i + 1), dp(i + 2)) + cost[i]
        return min(dp(0), dp(1))

    def minCostClimbingStairs_dp(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0] * (N + 2)
        for i in range(N - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        print(dp)
        return min(dp[0], dp[1])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)

        dp = [0, 0, 0]
        for i in range(N - 1, -1, -1):
            dp[2], dp[1] = dp[1], dp[0]
            dp[0] = cost[i] + min(dp[1], dp[2])
        return min(dp[0], dp[1])
