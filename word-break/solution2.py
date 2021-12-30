from test import checkTests
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        dp = [False] * (n+1)

        # Since all words must be followed another word
        dp[0] = True
        for j in range(1, n+1):
            for i in range(j):
                # dp[i] indicates the tail of the last word
                if dp[i] and s[i:j] in wordSet:
                    dp[j] = True
                    break
        return dp[-1]

checkTests(Solution().wordBreak)
