class Solution:
    #
    # Explanation:
    # https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/discuss/1717115/Backtracking-greater-Dynamic-Programming
    #
    def minimumDeleteSum_backtrack(self, s1: str, s2: str) -> int:
        lenS1, lenS2 = len(s1), len(s2)

        @lru_cache(2000)
        def dp(i: int, j: int) -> int:
            if (i == lenS1) or (j == lenS2):
                s = 0
                if (i == lenS1):
                    while(j < lenS2):
                        s += ord(s2[j])
                        j += 1
                else:
                    while(i < lenS1):
                        s += ord(s1[i])
                        i += 1
                return s

            if s1[i] == s2[j]:
                # Both characters are matched,
                # so no need to remove any characters
                return dp(i + 1, j + 1)
            else:
                return min(ord(s1[i]) + dp(i + 1, j),
                           ord(s2[j]) + dp(i, j + 1))
        return dp(0, 0)

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        lenS1, lenS2 = len(s1), len(s2)

        dp = [[0] * (lenS2 + 1) for _ in range(lenS1 + 1)]


        # Create base cases
        s = 0
        for i in range(lenS1 - 1, -1, -1):
            s += ord(s1[i])
            dp[i][lenS2] = s


        s = 0
        for i in range(lenS2 - 1, -1, -1):
            s += ord(s2[i])
            dp[lenS1][i] = s


        for i in range(lenS1 - 1, -1, -1):
            for j in range(lenS2 - 1, -1, -1):
                if s1[i] == s2[j]:
                    # Both characters are matched,
                    # so no need to remove any characters
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(ord(s1[i]) + dp[i + 1][j],
                                    ord(s2[j]) + dp[i][j + 1])

        for i in range(lenS1 + 1):
            print(dp[i])
        return dp[0][0]
