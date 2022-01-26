class Solution:
    def maxProfit_backtrack(self, prices: List[int], fee: int) -> int:
        N = len(prices)

        @cache
        def dp(i: int, hold: int) -> int:
            if (i == N):
                return 0

            doNothing = dp(i + 1, hold)

            doSomething = 0
            if (hold == 1):
                # We can sell stock
                doSomething = prices[i] - fee + dp(i + 1, 0)
            else:
                # We can buy stock
                doSomething = -prices[i] + dp(i + 1, 1)
            return max(doNothing, doSomething)
        return dp(0, 0)

    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)

        dp = [[0] * 2 for _ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            for hold in range(2):
                doNothing = dp[i + 1][hold]

                doSomething = 0
                if (hold == 1):
                    # We can sell stock
                    doSomething = prices[i] - fee + dp[i + 1][0]
                else:
                    # We can buy stock
                    doSomething = -prices[i] + dp[i + 1][1]
                dp[i][hold] = max(doNothing, doSomething)
        return dp[0][0]
