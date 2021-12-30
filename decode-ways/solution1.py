from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)

        @lru_cache(maxsize=None)
        def backtrack(i: int) -> int:
            if (i == N):
                return 1
            if (i > N) or (s[i] == "0"):
                return 0

            result = backtrack(i + 1)

            if 1 <= int(s[i:i+2]) <= 26:
                result += backtrack(i + 2)
            return result
        return backtrack(0)
