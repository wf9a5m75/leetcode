class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        M = len(matrix)
        N = len(matrix[0])

        dp = [[0] * (N + 1) for _ in range(M + 1)]

        ans = 0
        for y in range(M):
            for x in range(N):
                if matrix[y][x] == "1":
                    # pick the minumum side length from the top, top/left, and left, and add one
                    # (At least one "1")
                    #
                    # matrix   dp
                    #  1  1   0 0 0
                    #  1  1   0 0 0
                    #         0 0 0
                    # ---------------
                    # [1] 1   0 0 0
                    #  1  1   0 1 0
                    #         0 0 0
                    # ---------------
                    #  1 [1]  0 0 0
                    #  1  1   0 1 1
                    #         0 0 0
                    # ---------------
                    #  1  1   0 0 0
                    # [1] 1   0 1 1
                    #         0 1 0
                    # ---------------
                    #  1  1   0 0 0
                    #  1 [1]  0 1 1
                    #         0 1 2
                    #
                    dp[y + 1][x + 1] = min(dp[y][x + 1], dp[y + 1][x], dp[y][x]) + 1
                    ans = max(ans, dp[y + 1][x + 1])

        return ans * ans
