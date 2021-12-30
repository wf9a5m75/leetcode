class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0] * N

        def backtrack(i: int) -> int:
            if (i == N):
                return 1
            if (i > N):
                return 0
            if (s[i] == "0"):
                return 0
            if (dp[i] > 0):
                return dp[i]

            result = backtrack(i + 1)

            if 1 <= int(s[i:i+2]) <= 26:
                result += backtrack(i + 2)
            dp[i] = result
            return result
        return backtrack(0)
        
