class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        N = len(s)
        L = R = x = 0
        while(x < N):
            while(x < N) and (s[x] != " "):
                x += 1
            R = x - 1
            while(L < R):
                s[L], s[R] = s[R], s[L]
                L += 1
                R -= 1
            x += 1
            L = x
        return "".join(s)
                
