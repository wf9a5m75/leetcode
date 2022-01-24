class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)

        @lru_cache(2000)
        def dp(i: int, remainTransactions: int, holding: int) -> int:

            # We can't move ahead anymore
            if (i == N) or (remainTransactions == 0):
                return 0

            doNothing = dp(i + 1, remainTransactions, holding)

            doSomething = 0
            if holding == 1:
                # We sell stock
                doSomething = prices[i] + dp(i + 1, remainTransactions - 1, 0)
            else:
                # We buy stock
                doSomething = -prices[i] + dp(i + 1, remainTransactions, 1)

            # We choose the best option
            return max(doNothing, doSomething)

        return dp(0, k, 0)
