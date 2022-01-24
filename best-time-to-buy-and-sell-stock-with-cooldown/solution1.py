class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state variables
        #   cooldown : 0 -> no, 1 -> yes
        #   i : current index
        #   holding : 0 -> not holding stock (can buy)
        #             1 -> holding stock (can sell)

        N = len(prices)

        @lru_cache(2000)
        def dp(i: int, coolDown: int, holding: int) -> int:
            if (i == N):
                return 0

            doNothing = dp(i + 1, 0, holding)

            doSomething = 0
            if coolDown == 0:
                if holding == 0:
                    # buy stock
                    doSomething = -prices[i] + dp(i + 1, 0, 1)
                else:
                    # sell stock
                    doSomething = prices[i] + dp(i + 1, 1, 0)
            return max(doNothing, doSomething)

        return dp(0, 0, 0)
