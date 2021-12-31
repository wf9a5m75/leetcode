class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #
        # DP: Bottom-up
        #   O(MN)
        #
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        ans = 0
        for y in range(M):
            for x in range(N):
                if (text1[y] == text2[x]):
                    dp[y + 1][x + 1] = dp[y][x] + 1
                else:
                    dp[y + 1][x + 1] = max(dp[y + 1][x], dp[y][x + 1])
            ans = max(ans, dp[y][N])
        ans = max(ans, dp[M][N])

        return ans
