class Solution:
    def maxPower(self, s: str) -> int:
        L = 0
        N = len(s)
        ans = 0
        for R in range(N):
            if s[L] != s[R]:
                ans = max(ans, R - L)
                L = R
        ans = max(ans, R - L + 1)
        return ans
