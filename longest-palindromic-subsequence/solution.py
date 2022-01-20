class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0] * N for _ in range(N)]

        for y in range(N - 1, -1, -1):
            dp[y][y] = 1
            for x in range(y + 1, N):
                if (s[y] == s[x]):
                    dp[y][x] = dp[y + 1][x - 1] + 2
                else:
                    dp[y][x] = max(dp[y + 1][x], dp[y][x - 1])
        # for y in range(N):
        #     print(dp[y])
        return dp[0][N - 1]
