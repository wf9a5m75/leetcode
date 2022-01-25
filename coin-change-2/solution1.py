class Solution:
    def change_backtrack(self, amount: int, coins: List[int]) -> int:
        #
        # 1. DP(Top-down)
        #   time : O(N * amount)   N... number of coins
        #   space : O(N * amount)
        #
        N = len(coins)

        @cache
        def dp(i: int, amountSoFar: int) -> int:
            if (amountSoFar == amount):
                return 1
            if (i == N):
                return 0

            ways = dp(i + 1, amountSoFar)

            if (amountSoFar + coins[i] <= amount):
                ways += dp(i, amountSoFar + coins[i])
            return ways
        return dp(0, 0)

    def change_dp(self, amount: int, coins: List[int]) -> int:
        #
        # 2. DP(Bottom-Up)
        #   time : O(N * amount)   N... number of coins
        #   space : O(N * amount)
        #
        N = len(coins)
        dp = [[0] * (amount + 1) for _ in range(N + 1)]
        for i in range(N - 1, -1, -1):
            dp[i][amount] = 1
            dp[i + 1][amount] = 1

            for amountSoFar in range(amount, -1, -1):
                ways = dp[i + 1][amountSoFar]
                if (amountSoFar + coins[i] <= amount):
                    ways += dp[i][amountSoFar + coins[i]]
                dp[i][amountSoFar] = ways

        return dp[0][0]

    def change_slim(self, amount: int, coins: List[int]) -> int:
        #
        # 3. slimed down DP(Bottom-Up)
        #   time : O(N * amount)   N... number of coins
        #   space : O(amount)
        #
        N = len(coins)
        dp = [[0] * (amount + 1) for _ in range(2)]

        dp[0][amount] = dp[1][amount] = 1

        for i in range(N - 1, -1, -1):

            for amountSoFar in range(amount, -1, -1):
                ways = dp[1][amountSoFar]
                if (amountSoFar + coins[i] <= amount):
                    ways += dp[0][amountSoFar + coins[i]]
                dp[0][amountSoFar] = ways

            for amountSoFar in range(amount - 1, -1, -1):
                dp[1][amountSoFar] = dp[0][amountSoFar]
                dp[0][amountSoFar] = 0

        return dp[1][0]

    def change_more_slim(self, amount: int, coins: List[int]) -> int:
        #
        # 4. more slimed down DP(Bottom-Up)
        #   time : O(N * amount)   N... number of coins
        #   space : O(amount)
        #
        N = len(coins)
        dp = [0] * (amount + 1)

        dp[amount] = 1

        for i in range(N - 1, -1, -1):

            for amountSoFar in range(amount, -1, -1):
                ways = dp[amountSoFar]
                if (amountSoFar + coins[i] <= amount):
                    ways += dp[amountSoFar + coins[i]]
                dp[amountSoFar] = ways

        return dp[0]

    def change(self, amount: int, coins: List[int]) -> int:
        #
        # 5. speed optimized DP(Bottom-Up)
        #   time : O(N * amount)   N... number of coins
        #   space : O(amount)
        #
        N = len(coins)
        dp = [0] * (amount + 1)

        dp[amount] = 1
        for i in range(N - 1, -1, -1):
            for amountSoFar in range(amount - coins[i], -1, -1):
                dp[amountSoFar] += dp[amountSoFar + coins[i]]

        return dp[0]
