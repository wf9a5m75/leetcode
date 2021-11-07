class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        [2]
        [3, 4]
        [6, 5, 7]
        [4, 1, 8, 3]
        """
        INF = 2**31 - 1
        M = len(triangle)
        N = len(triangle[M - 1])
        dp = [[INF] * (m + 1) for m in range(M)]

        dp[0][0] = triangle[0][0]

        for m in range(M - 1):
            for i in range(m + 1):
                dp[m + 1][i] = min(dp[m + 1][i], dp[m][i] + triangle[m + 1][i])
                dp[m + 1][i + 1] = min(dp[m + 1][i + 1], dp[m][i] + triangle[m + 1][i + 1])
        ans = INF
        for i in range(M):
            ans = min(ans, dp[M - 1][i])
        return ans
