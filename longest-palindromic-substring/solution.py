class Solution:
    def longestPalindrome_matcher(self, s: str) -> str:
        #
        # (1) Since the matcher algorithm can detect only odd palindrome,
        #     bind each character with "#"(dummy character)
        s = "#{}#".format("#".join(s))


        n = len(s)
        ans = s[0]
        maxJ = 0

        # The variable R keeps how many characters are palindrome last time.
        R = [0] * n

        for i in range(n):

            # (2) Is there palindrome?
            #
            j = R[i]
            isPalindrome = True
            while(i - j >= 0) and (i + j < n) and (s[i - j] == s[i + j]):
                j += 1

            if j == R[i]:
                continue

            # (3) Keep the palindrome if longer than current
            if j > maxJ:
                ans = s[i - j + 1 : i + j]
                maxJ = j
                # print(ans, maxJ)


            # (4) Since we already know the same characters exist in mirror position,
            #  copy the information from left to right
            while(j > 0):
                j -= 1
                R[i + j] = R[i - j]

        # print(*R)
        return ans.replace("#", "")



    def longestPalindrome_dp(self, s: str) -> str:
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
                    
