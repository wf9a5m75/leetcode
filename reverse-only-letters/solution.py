class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        L, R = 0, len(s) - 1
        while(L < R):
            if (not s[L].isalpha()):
                L += 1
            if (not s[R].isalpha()):
                R -= 1

            if (s[L].isalpha() and s[R].isalpha()):
                s[L], s[R] = s[R], s[L]
                L += 1
                R -= 1
        return "".join(s)
