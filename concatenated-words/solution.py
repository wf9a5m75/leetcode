class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        #
        # https://leetcode.com/problems/concatenated-words/discuss/159348/Python-DFS-readable-solution
        #
        wordDict = set(words)

        dp = {}
        def dfs(s: str) -> List[str]:
            if s in dp:
                return dp[s]

            dp[s] = False

            N = len(s)
            for i in range(1, N):
                prefix = s[:i]
                suffix = s[i:]

                if (prefix in wordDict) and ((suffix in wordDict) or dfs(suffix)):
                    dp[s] = True
                    break
            return dp[s]

        results = []
        for word in words:
            if dfs(word):
                results.append(word)
        return results
