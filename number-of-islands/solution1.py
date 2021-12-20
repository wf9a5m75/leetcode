class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #
        # DFS approach
        #  Time complexity: O(M * N)
        #  Space complexity: O(M * N) for worst case
        #
        M, N = len(grid), len(grid[0])

        islands = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for y in range(M):
            for x in range(N):
                if (grid[y][x] == "1"):
                    islands += 1

                    queue = [(y,x)]
                    while(queue):
                        i,j = queue.pop(0)
                        if (grid[i][j] == "1"):
                            grid[i][j] = "0"
                            for dy, dx in directions:
                                if (0 <= i + dy < M):
                                    queue.append((i + dy, j))
                                if (0 <= j + dx < N):
                                    queue.append((i, j + dx))
            # print(*grid[y])

        return islands
