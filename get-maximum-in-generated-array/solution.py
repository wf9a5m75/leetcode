class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if (n == 0):
            return 0
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(1, n + 1):
            if (i * 2 <= n):
                dp[i * 2] = dp[i]
            if i * 2 + 1 <= n:
                dp[i * 2 + 1] = dp[i] + dp[i + 1]
        return max(dp)
