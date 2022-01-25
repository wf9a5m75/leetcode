class Solution:
    def coinChange_backtrack(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        INF = float("inf")

        @cache
        def dp(i: int, amountSoFar: int) -> int:
            if (amountSoFar == amount):
                return 0
            if (i == N):
                return INF

            # move on to the next coin
            doNothing = dp(i + 1, amountSoFar)

            # use the current coin
            doSomething = INF
            coinCnt = 0

            while(amountSoFar + coins[i] <= amount):
                amountSoFar += coins[i]
                coinCnt += 1
                doSomething = min(doSomething, coinCnt + dp(i + 1, amountSoFar))
            return min(doNothing, doSomething)
        return dp(0, 0)

    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        INF = float("inf")

        dp = [[INF] * (amount + 1) for _ in range(N + 1)]

        # for i in range(amount + 1):
        #     print(dp[i])

        for i in range(N - 1, -1, -1):
            dp[i + 1][amount] = 0

            for amountSoFar in range(amount, -1, -1):
                # move on to the next coin
                doNothing = dp[i + 1][amountSoFar]

                # use the current coin
                doSomething = INF
                if amountSoFar + coins[i] <= amount:
                    doSomething = min(doSomething, dp[i][amountSoFar + coins[i]] + 1)

                dp[i][amountSoFar] = min(doSomething, doNothing)
        return dp[0][0] if dp[0][0] != INF else -1
                
