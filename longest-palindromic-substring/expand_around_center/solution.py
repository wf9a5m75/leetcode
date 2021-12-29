class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        ans = ""
        for i in range(N):

            # Since one character is valid palindrom,
            # so s[i] is always True.
            L = R = i

            # There is a possibility to consective same character, (i.e. "bbbbbb"),
            # so we expand R as much as possible.
            while(R < N) and (s[L] == s[R]):
                R += 1
            R -= 1

            # If the substring s[L:R + 1] is palindrom, s[L] should be the same with s[R].
            # We expand L and R one by one.
            while (L >= 0) and (R < N) and (s[L] == s[R]):
                L -= 1
                R += 1
            if (len(ans) < (R - L - 1)):
                ans = s[L + 1:R]
        return ans
