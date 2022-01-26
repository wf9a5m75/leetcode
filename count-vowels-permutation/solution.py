class Solution:
    #
    # https://leetcode.com/problems/count-vowels-permutation/discuss/1720656/Explanation-of-DP-step-by-step-(for-myself)
    #
    def countVowelPermutation_backtrack(self, n: int) -> int:
        charA, charE, charI, charO, charU = 0,1,2,3,4
        MOD = 1000000007

        @cache
        def dp(i : int, prev : int)->int:
            if i == n:
                return 1

            ways = 0
            if prev == charA:
                ways = dp(i + 1, charE)
                ways += dp(i + 1, charI)
                ways += dp(i + 1, charU)

            elif prev == charE:
                ways = dp(i + 1, charA)
                ways += dp(i + 1, charI)

            elif prev == charI:
                ways = dp(i + 1, charO)
                ways += dp(i + 1, charE)

            elif prev == charO:
                ways = dp(i + 1, charI)

            else:
                ways = dp(i + 1, charO)
                ways += dp(i + 1, charI)

            return ways

        ways = 0
        for i in range(5):
            ways += dp(1, i)
        return ways % MOD

    def countVowelPermutation_dp(self, n: int) -> int:
        charA, charE, charI, charO, charU = 0,1,2,3,4
        MOD = 1000000007

        dp = [[0] * 5 for _ in range(n + 1)]
        for i in range(5):
            dp[n][i] = 1

        for i in range(n - 1, 0, -1):
            for prev in range(5):

                ways = 0
                if prev == charA:
                    ways = dp[i + 1][charE]
                    ways += dp[i + 1][charI]
                    ways += dp[i + 1][charU]

                elif prev == charE:
                    ways = dp[i + 1][charA]
                    ways += dp[i + 1][charI]

                elif prev == charI:
                    ways = dp[i + 1][charO]
                    ways += dp[i + 1][charE]

                elif prev == charO:
                    ways = dp[i + 1][charI]

                else:
                    ways = dp[i + 1][charO]
                    ways += dp[i + 1][charI]
                dp[i][prev] = ways % MOD

        ways = 0
        for i in range(5):
            ways += dp[1][i]

        return ways % MOD

    def countVowelPermutation(self, n: int) -> int:
        charA, charE, charI, charO, charU = 0,1,2,3,4
        MOD = 1000000007

        dp = [1,1,1,1,1]

        actions = [
            lambda prevDp: prevDp[charE] + prevDp[charI] + prevDp[charU],
            lambda prevDp: prevDp[charA] + prevDp[charI],
            lambda prevDp: prevDp[charO] + prevDp[charE],
            lambda prevDp: prevDp[charI],
            lambda prevDp: prevDp[charI] + prevDp[charO]
        ]

        for i in range(n - 1, 0, -1):
            prevDp = dp.copy()
            for prev in range(5):
                dp[prev] = actions[prev](prevDp) % MOD

        ways = 0
        for prev in range(5):
            ways += dp[prev]
        return ways % MOD
