class Solution:
    def change_backtrack(self, amount: int, coins: List[int]) -> int:

        N = len(coins)

        @cache
        def dp(i: int, amountSoFar: int) -> int:
            if amountSoFar == amount:
                return 1
            if i == N:
                return 0

            # We don't use this coin
            coinCnt = dp(i + 1, amountSoFar)

            # We use this coin
            if coins[i] + amountSoFar <= amount:
                coinCnt += dp(i, coins[i] + amountSoFar)

            return coinCnt
        return dp(0, 0)

    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)

        dp = [[0] * (amount + 1) for _ in range(N + 1)]

        dp[0][amount] = 1
        for i in range(N - 1, -1, -1):
            dp[i + 1][amount] = 1

            for amountSoFar in range(amount, -1, -1):
                # We don't use this coin
                dp[i][amountSoFar] = dp[i + 1][amountSoFar]

                # We use this coin
                if coins[i] + amountSoFar <= amount:
                    dp[i][amountSoFar] += dp[i][coins[i] + amountSoFar]
        return dp[0][0]

    
