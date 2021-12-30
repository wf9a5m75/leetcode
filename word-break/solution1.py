from test import checkTests
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Build a trie tree
        dic = {}
        for word in wordDict:
            parent = dic
            for w in word:
                if w not in parent:
                    parent[w] = {}
                parent = parent[w]
            parent["eow"] = word

        N = len(s)
        dp = [False] * (N + 1)

        # Since the last word has to meet dp[j + 1] = True,
        # we set dp[N] = True
        dp[N] = True

        for i in range(N - 1, -1, -1):
            parent = dic
            for j in range(i, N):
                if s[j] in parent:
                    parent = parent[s[j]]

                    # dp[j + 1] = True if another word starts from s[j + 1].
                    # We must place words consectively,
                    # so all words must meet next word.
                    if ("eow" in parent) and (dp[j + 1]):
                        dp[i] = True
                        # print(parent["eow"]) # debug
                        break
                else:
                    # If s[j] does not hit, break the loop.
                    break
        # If all words fit to s, dp[0] should be True
        return dp[0]

checkTests(Solution().wordBreak)
