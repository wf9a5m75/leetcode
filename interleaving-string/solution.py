class Solution:
    def isInterleave_backtrack(self, s1: str, s2: str, s3: str) -> bool:

        lenS1, lenS2 = len(s1), len(s2)

        @cache
        def dp(i: int, j: int) -> bool:
            if (i == lenS1) or (j == lenS2):
                while(j < lenS2) and (s2[j] == s3[i + j]):
                    j += 1
                while(i < lenS1) and (s1[i] == s3[i + j]):
                    i += 1

                return (i == lenS1) and (j == lenS2)

            result = False
            if (i < lenS1) and (s1[i] == s3[i + j]):
                result = dp(i + 1, j)

            if (result == False) and (j < lenS2) and (s2[j] == s3[i + j]):
                result = dp(i, j + 1)
            return result
        return dp(0, 0)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        lenS1, lenS2, lenS3 = len(s1), len(s2), len(s3)
        if (lenS1 + lenS2 != lenS3):
            return False

        dp = [[False] * (lenS2 + 1) for _ in range(lenS1 + 1)]

        dp[lenS1][lenS2] = True
        # Create base cases
        i = lenS1 - 1
        j = len(s3) - 1
        while(i >= 0) and (j >= 0) and (s1[i] == s3[j]):
            dp[i][lenS2] = True
            i -= 1
            j -= 1
        i = lenS2 - 1
        j = len(s3) - 1
        while(i >= 0) and (j >= 0) and (s2[i] == s3[j]):
            dp[lenS1][i] = True
            i -= 1
            j -= 1

        for i in range(lenS1 - 1, -1, -1):
            for j in range(lenS2 - 1, -1, -1):

                result = False
                if (i < lenS1) and (s1[i] == s3[i + j]):
                    result = dp[i + 1][j]
                if (result == False) and (j < lenS2) and (s2[j] == s3[i + j]):
                    result = dp[i][j + 1]
                dp[i][j] = result

        return dp[0][0]
