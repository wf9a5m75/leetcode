class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)

        dp = [[[0] * 2 for _ in range(k + 1)] for __ in range(N + 1)]
        for i in range(N - 1, -1, -1):
            for remainTransactions in range(1, k + 1):
                for holding in range(2):
                    doNothing = dp[i + 1][remainTransactions][holding]

                    doSomething = 0
                    if holding == 1:
                        # We sell stock
                        doSomething = prices[i] + dp[i + 1][remainTransactions - 1][0]
                    else:
                        # We buy stock
                        doSomething = -prices[i] + dp[i + 1][remainTransactions][1]
                    dp[i][remainTransactions][holding ] = max(doNothing, doSomething)
        return dp[0][k][0]
