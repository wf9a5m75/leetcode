class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0

        m1, n1 = m + 1, n + 1
        dp = [[0] * n1 for _ in range(m1)]

        dp[0][0] = 1
        for y in range(m):
            for x in range(n):

                # If there is no obstacle at (y + 1, x),
                # copy the current unique path to the current
                if (y + 1 < m)  and (obstacleGrid[y + 1][x] == 0):
                    dp[y + 1][x] = max(dp[y + 1][x], dp[y][x])

                # If there is no obstacle at (y, x + 1),
                # copy the current unique path to the current
                if (x + 1 < n)  and (obstacleGrid[y][x + 1] == 0):
                    dp[y][x + 1] = max(dp[y][x + 1], dp[y][x])

                # The diagnal cell (i.e. <1,1> from <0,0>), there are two way approaches:
                #    1) origin -> right -> down
                #    2) and origin -> down -> right
                # So, both sums up.
                if (y + 1 < m)  and (x + 1 < n)  and (obstacleGrid[y + 1][x + 1] == 0):
                    dp[y + 1][x + 1] = max(dp[y][x + 1] + dp[y + 1][x], dp[y + 1][x + 1])

        # for row in dp:
        #     print(*row)
        return dp[m - 1][n - 1]
