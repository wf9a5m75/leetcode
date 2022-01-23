class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[N] = True

        for i in range(N - 1, -1, -1):
            for word in wordDict:
                wLen = len(word)
                if (i+wLen - 1 < N):
                    # print(i, s[i:i+wLen - 1], word, dp[i + wLen])
                    if (s[i:i+wLen] == word) and dp[i + wLen]:
                        dp[i] = True
        # print(dp)
        return dp[0]
