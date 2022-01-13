class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        for word in wordDict:
            parent = trie
            for w in word:
                if w not in parent:
                    parent[w] = {
                        "eow": False
                    }
                parent = parent[w]
            parent["eow"] = True

        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True

        for i in range(N):
            # Since all words must be followed by another word,
            # we move the pointer to the next EOW(dp[i] = True)
            if (dp[i] == False):
                continue

            # We try to find all words from i.
            # If we found the eow (end of word), records the positions
            parent = trie
            j = i
            while(j < N) and (s[j] in parent):
                parent = parent[s[j]]
                dp[j + 1] = dp[j + 1] | parent["eow"]
                j += 1

        #print(dp)
        return dp[N]
