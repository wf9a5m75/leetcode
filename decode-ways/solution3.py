class Solution:
    def numDecodings_backtrack(self, s: str) -> int:
        N = len(s)

        @cache
        def dp(i : int) -> int:
            if (i == N):
                return 1
            if s[i] == "0":
                return 0

            ways = 0
            if (s[i] == "1") and (i + 1 < N):
                ways += dp(i + 2)
            elif (s[i] == "2") and (i + 1 < N) and (int(s[i + 1]) < 7):
                ways += dp(i + 2)

            ways += dp(i + 1)
            return ways
        return dp(0)

    def numDecodings_dp(self, s: str) -> int:
        N = len(s)
        dp = [0] * (N + 1)
        dp[N] = 1
        for i in range(N - 1, -1, -1):
            if (s[i] == "0"):
                continue

            ways = 0
            if (s[i] == "1") and (i + 1 < N):
                ways += dp[i + 2]
            elif (s[i] == "2") and (i + 1 < N) and (int(s[i + 1]) < 7):
                ways += dp[i + 2]
            dp[i] = ways + dp[i + 1]
        return dp[0]

    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [1, 1, 0]
        for i in range(N - 1, -1, -1):
            dp[0], dp[1], dp[2] = 0, dp[0], dp[1]

            if (s[i] == "0"):
                continue

            ways = 0
            if (s[i] == "1") and (i + 1 < N):
                ways += dp[2]
            elif (s[i] == "2") and (i + 1 < N) and (int(s[i + 1]) < 7):
                ways += dp[2]
            dp[0] = ways + dp[1]
        return dp[0]

        
