class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        N = len(s)
        dp = [[] for _ in range(N + 1)]
        dp[N] = [""]


        for i in range(N - 1, -1, -1):
            for word in wordDict:
                wLen = len(word)
                if (i+wLen - 1 < N):
                    # print(i, s[i:i+wLen - 1], word, dp[i + wLen])
                    if (s[i:i+wLen] == word) and (len(dp[i + wLen]) > 0):
                        for prevS in dp[i + wLen]:
                            if i + wLen == N:
                                dp[i].append(word)
                            else:
                                dp[i].append(word + " " + prevS)
        # print(dp)
        return dp[0]
