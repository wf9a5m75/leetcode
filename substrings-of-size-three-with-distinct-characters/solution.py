class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        N = len(s)
        L = 0
        R = 2
        ans = 0
        while(R < N):
            subs = s[L:R + 1]
            if (len(set(subs)) == 3):
                ans += 1
            L += 1
            R += 1
        return ans
