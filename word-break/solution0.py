from test import checkTests
from typing import List
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        for word in wordDict:
            parent = dic
            for w in word:
                if w not in parent:
                    parent[w] = {}
                parent = parent[w]
            parent["eow"] = True

        N = len(s)

        @lru_cache()
        def backtrack(i: int) -> bool:
            if (i == N):
                return True

            parent = dic
            while(i < N) and (s[i] in parent):
                if (s[i] in parent):
                    parent = parent[s[i]]
                else:
                    return False

                if "eow" in parent:
                    if (backtrack(i + 1)):
                        return True
                i += 1
            return False
        return backtrack(0)

checkTests(Solution().wordBreak)
