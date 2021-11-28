class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if (N == 0) or (grid[0][0] == 1) or (grid[N - 1][N - 1] == 1):
            return -1

        queue = [(0, 0, 0)]
        while(queue):
            step, y, x = queue.pop(0)

            if grid[y][x] != 0:
                continue
            if (y == N - 1) and (x == N - 1):
                return step + 1

            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (dx == 0) and (dy == 0):
                        continue
                    if ((0 <= y + dy < N) and (0 <= x + dx < N)
                        and (grid[y + dy][x + dx] == 0)):
                        queue.append((step + 1, y + dy, x + dx))
            grid[y][x] = 2
        return -1
    
