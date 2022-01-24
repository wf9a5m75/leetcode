class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lenText1, lenText2 = len(text1), len(text2)
        dp = [[0] * (lenText2 + 1) for _ in range(lenText1 + 1)]

        for i in range(lenText1 - 1, -1, -1):
            for j in range(lenText2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]


    def longestCommonSubsequence_tle(self, text1: str, text2: str) -> int:
        #
        # (1) Write a code with backtracking, then
        # (2) convert it to the DP bottom-up
        #
        lenText1, lenText2 = len(text1), len(text2)
        @lru_cache(2000)
        def dp(i: int, j: int) -> int:
            if (i == lenText1) or (j == lenText2):
                return 0

            doSomething = 0
            if text1[i] == text2[j]:
                doSomething = 1 + dp(i + 1, j + 1)
            else:
                doSomething = max(dp(i + 1, j), dp(i, j + 1))
            return doSomething
        return dp(0, 0)
