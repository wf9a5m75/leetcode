class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        #
        # DP approach
        #    https://leetcode.com/problems/minimum-falling-path-sum-ii/discuss/1698083/Python-or-DP-or-easy-to-understand
        #
        #    Time complexity: O(N * N)
        #    Space complexity: O(N)
        #
        N = len(grid)
        INF = float("inf")

        for y in range(N - 1):
            dpL = [INF] * N
            dpR = dpL.copy()

            for x in range(N - 1):
                dpL[x + 1] = min(dpL[x], grid[y][x])
                dpR[N - 2 - x] = min(dpR[N - 1- x], grid[y][N - 1 - x])

            for x in range(N):
                grid[y + 1][x] += min(dpL[x], dpR[x])

        return min(grid[N - 1])
