import sys
from io import StringIO

class Solution:
    def reverseVowels(self, s: str) -> str:
        L = 0
        R = len(s) - 1

        vowels = "aiueoAIUEO"
        s = list(s)
        while(L < R):
            while(L <= R) and (s[L] not in vowels):
                L+=1
            while(L <= R) and (s[R] not in vowels):
                R-=1
            if (L > R):
                break
            s[L], s[R] = s[R], s[L]
            L+=1
            R-=1
        return "".join(s)
