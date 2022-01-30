class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        @cache
        def dp(i: int, remain: int, isHolding: int) -> int:
            if (remain == 0) or (i == N):
                return 0

            doNothing = dp(i + 1, remain, isHolding)

            doSomething = 0
            if (isHolding == 1):
                doSomething = prices[i] + dp(i + 1, remain - 1, 0)
            else:
                doSomething = -prices[i] + dp(i + 1, remain, 1)
            return max(doNothing, doSomething)
        return dp(0, 2, 0)

    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        dp = [[[0] * 2 for _ in range(3)] for __ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            for remain in range(1, 3):
                for isHolding in range(2):
                    doNothing = dp[i + 1][remain][isHolding]
                    doSomething = 0
                    if (isHolding == 1):
                        doSomething = prices[i] + dp[i + 1][remain - 1][0]
                    else:
                        doSomething = -prices[i] + dp[i + 1][remain][1]
                    dp[i][remain][isHolding] = max(doNothing, doSomething)
        return dp[0][2][0]

    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        dp = [[[0] * 2 for _ in range(3)] for __ in range(2)]

        prevIdx = 1
        currIdx = 0

        for i in range(N - 1, -1, -1):
            for remain in range(1, 3):
                for isHolding in range(2):
                    doNothing = dp[prevIdx][remain][isHolding]
                    doSomething = 0
                    if (isHolding == 1):
                        doSomething = prices[i] + dp[prevIdx][remain - 1][0]
                    else:
                        doSomething = -prices[i] + dp[prevIdx][remain][1]
                    dp[currIdx][remain][isHolding] = max(doNothing, doSomething)
            prevIdx, currIdx = currIdx, prevIdx
        return dp[prevIdx][2][0]
