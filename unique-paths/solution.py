class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #------
        # DP approach
        #------

        n1 = n + 1
        m1 = m + 1
        dp = [[0] * n1 for i in range(m1)]

        dp[0][0] = 1

        for y in range(m):
            for x in range(n):
                dp[y + 1][x] = max(dp[y][x], dp[y + 1][x])
                dp[y][x + 1] =  max(dp[y][x], dp[y][x + 1])
                dp[y + 1][x + 1] = dp[y][x + 1] + dp[y + 1][x]

        return dp[m - 1][n - 1]

    def uniquePaths_backtracking(self, m: int, n: int) -> int:

        #------
        # This code gets the time limit error
        #------

        def walker(x, y):
            if (x == n) and (y == m):
                return 1

            result = 0
            if (x < n):
                result += walker(x + 1, y)
            if (y < m):
                result += walker(x, y + 1)

            return result

        return walker(1, 1)
