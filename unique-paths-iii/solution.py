class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        def walker(y: int, x: int, nonObstacleCellCnt: int, path: List[tuple]) -> int:
            path.append((y, x))
            print(nonObstacleCellCnt,  path)

            if (grid[y][x] == 2):
                if (nonObstacleCellCnt == 1):
                    print("Goal!")
                    path.pop()
                    return 1
                else:
                    print("too early!", nonObstacleCellCnt)
                    path.pop()
                    return 0

            if (grid[y][x] == -1):
                path.pop()
                return 0


            grid[y][x] = -1

            # Can we go each directions?
            result = 0
            # right
            if (x + 1 < N):
                result += walker(y, x + 1, nonObstacleCellCnt - 1, path)

            # down
            if (y + 1 < M):
                result += walker(y + 1, x, nonObstacleCellCnt - 1, path)

            # up
            if (y > 0):
                result += walker(y - 1, x, nonObstacleCellCnt - 1, path)

            # left
            if (x > 0):
                result += walker(y, x - 1, nonObstacleCellCnt - 1, path)

            grid[y][x] = 0
            path.pop()
            return result


        # Find the starting point
        startPoint = None
        nonObstacleCellCnt = 0
        for y in range(M):
            for x in range(N):
                if grid[y][x] == 1:
                    startPoint = (y, x)

                if grid[y][x] != -1:
                    nonObstacleCellCnt += 1
        return walker(startPoint[0], startPoint[1], nonObstacleCellCnt, [])
