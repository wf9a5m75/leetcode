class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        N = len(coins)
        INF = float("inf")
        dp = [[INF] * (amount + 1) for _ in range(N + 1)]


        for i in range(N):
            dp[i][0] = 0

            coin = coins[i]
            # if coin > amount:
            #     continue

            for j in range(amount + 1):
                dp[i + 1][j] = dp[i][j]
                if (j >= coin):
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i + 1][j - coin] + 1)


        return dp[N][amount] if dp[N][amount] != INF else -1
