class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1] * 5 for _ in range(n + 1)]

        for j in range(n - 1):
            for i in range(3, -1, -1):
                dp[j + 1][i] = dp[j][i] + dp[j + 1][i + 1]
        return sum(dp[n - 1])
