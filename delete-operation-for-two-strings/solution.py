class Solution:
    #
    #  Explanation
    #  https://leetcode.com/problems/delete-operation-for-two-strings/discuss/1717012/Python-or-creating-a-DP-from-backtracking
    #
    def minDistance_backtrack(self, word1: str, word2: str) -> int:

        lenWord1, lenWord2 = len(word1), len(word2)

        @lru_cache(2000)
        def dp(i: int, j: int) -> int:
            if (i == lenWord1) or (j == lenWord2):
                return abs(i - j)

            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            else:
                return 1 + min(dp(i + 1, j), dp(i, j + 1))
        return dp(0, 0)

    def minDistance(self, word1: str, word2: str) -> int:
        lenWord1, lenWord2 = len(word1), len(word2)

        dp = [[0] * (lenWord2 + 1) for _ in range(lenWord1 + 1)]

        # Base cases
        #
        # word1 = "te", word2 = "tea"
        #
        #     t  e  a
        #  t [0, 0, 0, 2]
        #  e [0, 0, 0, 1]
        #    [3, 2, 1, 0]
        #
        for i in range(lenWord1 + 1):
            dp[i][lenWord2] = lenWord1 - i
        for j in range(lenWord2 + 1):
            dp[lenWord1][j] = lenWord2 - j

        for i in range(lenWord1 - 1, -1, -1):
            for j in range(lenWord2 - 1, -1, -1):

                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
