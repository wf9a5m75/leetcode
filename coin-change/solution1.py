class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        N = len(coins)
        INF = float("inf")
        dp = [INF] * (amount + 1)
        dp[0] = 0


        for i in range(N):
            coin = coins[i]
            for j in range(amount + 1):
                if (j >= coin):
                    dp[j] = min(dp[j], dp[j - coin] + 1)


        return dp[amount] if dp[amount] != INF else -1
