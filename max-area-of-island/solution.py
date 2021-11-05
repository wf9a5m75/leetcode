class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        maxArea = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for y in range(M):
            for x in range(N):
                if (grid[y][x] == 1):
                    # count up the adjustive "1" cells in four directions
                    area = 0
                    queue = [(y, x)]
                    while(queue):
                        y,x = queue.pop(0)
                        if (grid[y][x] != 1):
                            continue
                        area += 1
                        grid[y][x] = 2
                        for direction in directions:
                            dy = y + direction[0]
                            dx = x + direction[1]
                            if ((0 <= dx < N) and
                                (0 <= dy < M) and
                                (grid[dy][dx] == 1)):
                                queue.append((dy, dx))
                    maxArea = max(maxArea, area)
        return maxArea
