class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])

        negative_color = -color
        orgColor = grid[row][col]

        # If new color is the same, just returns it.
        if orgColor == color:
            return grid

        queue = [(row, col)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while(queue):
            y,x = queue.pop(0)

            if (grid[y][x] < 0):
                # Skip visited cell
                continue

            if (y == 0) or (y == M - 1) or (x == 0) or (x == N - 1):
                if (grid[y][x] == orgColor):
                    # The same color on a border of the grid
                    grid[y][x] = negative_color
                else:
                    # Different color on a border of the grid
                    grid[y][x] = -grid[y][x]
            else:
                # Fill with new color if this cell faces any different color
                isOnEdge = False
                for delta in directions:
                    dy, dx = y + delta[0], x + delta[1]
                    if (grid[dy][dx] > 0) and (grid[dy][dx] != orgColor):
                        isOnEdge = True
                        break

                if (isOnEdge):
                    grid[y][x] = negative_color
                else:
                    grid[y][x] = -grid[y][x]

            # Continue searching on the adjacent cells with the same original color
            for delta in directions:
                dy, dx = y + delta[0], x + delta[1]
                if (0 <= dy < M) and (0 <= dx < N) and (grid[dy][dx] == orgColor):
                    queue.append((dy, dx))

        for y in range(M):
            for x in range(N):
                grid[y][x] = abs(grid[y][x])
        return grid
