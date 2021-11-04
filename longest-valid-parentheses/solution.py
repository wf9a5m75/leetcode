class Solution:
    def longestValidParentheses(self, s: str) -> int:
        i = 0
        N = len(s)
        L = R = 0
        ans = 0
        for c in s:
            if (c == "("):
                L += 1
            else:
                R += 1
            if (L == R):
                ans = max(ans, R * 2)
            elif (R >= L):
                L = R = 0

        L = R = 0
        for c in reversed(s):
            if (c == "("):
                L += 1
            else:
                R += 1
            if (L == R):
                ans = max(ans, L * 2)
            elif (L >= R):
                L = R = 0

        return ans

    def longestValidParentheses_slow(self, s: str) -> int:
        i = 0
        N = len(s)
        dp = [False] * N
        while(i < N):
            R = 0
            L = 1

            while(i - L >= 0) and (dp[i - L]):
                L += 1
            while (i + R < N) and (i - L >= 0) and (s[i - L] == "(") and (s[i + R] == ")"):
                dp[i - L] = dp[i + R] = True
                R += 1
                L += 1
            if (R == 0):
                i += 1
            else:
                i += R

        cnt = 0
        ans = 0
        for i in dp:
            if i:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
        ans = max(ans, cnt)

        return ans
