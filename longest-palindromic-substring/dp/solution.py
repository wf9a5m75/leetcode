class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # All single characters becomes one palindrome at least.
        ansStart = ansEnd = 0
        maxLength = 1
        for i in range(n):
            dp[i][i] = 1

        # If the same characters are consecutive, it's palindrome
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                ansStart = i
                ansEnd = i + 1
                maxLength = 2

        # From here, we will check k steps
        k = 0
        while(k < n):
            i = 0
            while(i < n - 1) and (i < k):
                if (dp[i + 1][k - 1]) and s[i] == s[k]:
                    # Put the same character at the mirroring position
                    dp[i][k] = dp[i + 1][k - 1]

                #
                if dp[i][k] and (k - i + 1 > maxLength):
                    ansStart = i
                    ansEnd = k
                    maxLength = ansEnd - ansStart + 1
                i+= 1
            k+=1


        # for row in dp:
        #     print(*row)

        return s[ansStart: ansEnd + 1]
