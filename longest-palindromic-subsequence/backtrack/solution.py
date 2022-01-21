class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def backtrack(txt: str) -> int:
            if txt == txt[::-1]:
                return len(txt)

            chars = set(txt)
            maxLen = 0
            for char in chars:
                L = txt.find(char)
                R = txt.rfind(char)
                if L == R:
                    maxLen = max(maxLen, 1)
                else:
                    maxLen = max(maxLen, backtrack(txt[L + 1: R]) + 2)
            return maxLen
        return backtrack(s)
