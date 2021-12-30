class Solution:
    def numDecodings(self, s: str) -> int:
        #
        # DP top-down
        #

        N = len(s)
        dp = [0] * (N + 1)

        # The number of ways to reach to index 0 is only one way.
        dp[0] = 1

        for i in range(1, N + 1):

            # If we can reach to this i from i - 1,
            # copy the number of the ways.
            if (s[i - 1] != "0"):
                dp[i] = dp[i - 1]

            # If we can reach to this i from i - 2,
            # adds up the number of the ways.
            if (i > 1) and (s[i - 2] != "0") and (int(s[i - 2:i]) <= 26):
                dp[i] += dp[i - 2]

        return dp[N]
