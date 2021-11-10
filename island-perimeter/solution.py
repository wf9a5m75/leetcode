class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        M, N = len(grid), len(grid[0])
        for y in range(M):
            for x in range(N):
                if (grid[y][x] == 1):

                    for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        dy, dx = y + delta[0], x + delta[1]
                        hasEdge = 1
                        if (0 <= dy < M) and (0 <= dx < N) and (grid[dy][dx] == 1):
                            hasEdge = 0
                        perimeter += hasEdge

        return perimeter
