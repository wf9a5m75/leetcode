class Solution:
    def numRollsToTarget_backtrack(self, n: int, k: int, target: int) -> int:
        MOD = 1000000007
        @cache
        def dp(i: int, sumSoFar: int)-> int:
            if (i == n):
                return int(sumSoFar == target)
            if (sumSoFar == target):
                return 0

            ways = 0
            j = 1
            while (j <= k) and (j + sumSoFar <= target):
                ways += dp(i + 1, j + sumSoFar) % MOD
                j += 1

            return ways % MOD
        return dp(0, 0)
    def numRollsToTarget_dp(self, n: int, k: int, target: int) -> int:
        MOD = 1000000007

        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[n][target] = 1

        for i in range(n - 1, -1, -1):
            for sumSoFar in range(target, -1, -1):
                ways = 0

                j = 1
                while (j <= k) and (j + sumSoFar <= target):
                    ways = (ways + dp[i + 1][j + sumSoFar]) % MOD

                    j += 1

                dp[i][sumSoFar] = ways % MOD

        return dp[0][0]
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1000000007

        dp = [0] * (target + 1)
        dp[target] = 1

        for i in range(n - 1, -1, -1):
            prevDp = dp.copy()
            for sumSoFar in range(target, -1, -1):
                ways = 0

                j = 1
                while (j <= k) and (j + sumSoFar <= target):
                    ways = (ways + prevDp[j + sumSoFar]) % MOD

                    j += 1

                dp[sumSoFar] = ways % MOD

        return dp[0]
