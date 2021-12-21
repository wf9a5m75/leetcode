class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #
        #  BSF approach
        #
        N = len(grid)
        if (grid[0][0] == 1) or (grid[N - 1][N - 1] == 1):
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        queue = [(0, 0, 1)]
        while(queue):
            nextQ = []
            while(queue):
                y, x, steps = queue.pop(0)
                if grid[y][x] != 0:
                    continue
                grid[y][x] = 1
                if (y == N - 1) and (x == N - 1):
                    return steps

                for direct in directions:
                    dy, dx = y + direct[0], x + direct[1]
                    if (0 <= dy < N) and (0 <= dx < N) and (grid[dy][dx] == 0):
                        nextQ.append((dy, dx, steps + 1))
            queue = nextQ

        # for y in range(N):
        #     print(*grid[y])

        return -1
