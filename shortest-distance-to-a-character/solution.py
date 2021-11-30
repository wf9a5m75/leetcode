class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        N = len(s)
        L = scoreL = scoreR = 0
        R = N - 1
        ans = [0] * N

        scoreL = N
        for L in range(N):
            if (s[L] == c):
                scoreL = 0
            else:
                scoreL += 1
            ans[L] = scoreL

        scoreR = N
        for R in range(N - 1, -1, -1):
            if (s[R] == c):
                scoreR = 0
            else:
                scoreR += 1
            ans[R] = min(ans[R], scoreR)
        return ans
