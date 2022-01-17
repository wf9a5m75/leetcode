class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        #
        # Heap queue
        #   Time complexity: O(N * NlogN)
        #   Space complexity: O(N)
        # https://leetcode.com/problems/minimum-falling-path-sum-ii/discuss/1698083/Python-or-DP-or-easy-to-understand
        #
        N = len(grid)

        for y in range(N - 1):
            twoMins = heapq.nsmallest(2, grid[y])

            for x in range(N):
                if (twoMins[0] == grid[y][x]):
                    grid[y + 1][x] += twoMins[1]
                else:
                    grid[y + 1][x] += twoMins[0]

        return min(grid[N - 1])
