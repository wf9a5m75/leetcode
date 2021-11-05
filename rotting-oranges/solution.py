class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # ------------------
        #  BFS approach
        # ------------------
        M, N = len(grid), len(grid[0])
        rottenOranges = []
        freshOrangeCnt = 0
        for y in range(M):
            for x in range(N):
                if grid[y][x] == 2:
                    rottenOranges.append((y, x))
                elif grid[y][x] == 1:
                    freshOrangeCnt += 1


        if (freshOrangeCnt > 0) and (len(rottenOranges) == 0):
            return -1
        elif (freshOrangeCnt == 0) and (len(rottenOranges) > 0):
            return 0


        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cnt = 0
        hasChanged = True
        while(rottenOranges) and (hasChanged):
            hasChanged = False
            nextRottenOranges = []
            while(rottenOranges):
                y, x = rottenOranges.pop(0)
                for delta in directions:
                    dy, dx = y + delta[0], x + delta[1]
                    if (0 <= dy < M) and (0 <= dx < N) and (grid[dy][dx] == 1):
                        grid[dy][dx] = 2
                        nextRottenOranges.append((dy, dx))
                        hasChanged = True
                        freshOrangeCnt -= 1
            rottenOranges = nextRottenOranges
            if (hasChanged):
                cnt += 1
            elif freshOrangeCnt > 0:
                return -1
        return cnt

    def orangesRotting_dp(self, grid: List[List[int]]) -> int:
        # ------------------
        #  DP approach
        # ------------------
        M, N = len(grid), len(grid[0])

        freshOrangeCnt = 0
        rottenOrangeCnt = 0
        for y in range(M):
            for x in range(N):
                if grid[y][x] == 1:
                    freshOrangeCnt += 1

                    hasBottom = True if (y + 1 < M) and (grid[y + 1][x] != 0) else False
                    hasRight = True if (x + 1 < N) and (grid[y][x + 1] != 0) else False
                    hasLeft = True if (x - 1 >= 0) and (grid[y][x - 1] != 0) else False
                    hasTop= True if (y - 1 >= 0) and (grid[y - 1][x] != 0) else False
                    if hasBottom == hasRight == hasLeft == hasTop == False:
                        return -1
                elif grid[y][x] == 2:
                    rottenOrangeCnt += 1


        if (freshOrangeCnt > 0) and (rottenOrangeCnt == 0):
            return -1
        elif (freshOrangeCnt == 0) and (rottenOrangeCnt > 0):
            return 0

        cnt = 0
        markRottenOrange = 2
        prevFreshOrangeCnt = -1
        while(freshOrangeCnt > 0):
            if (prevFreshOrangeCnt == freshOrangeCnt):
                return -1
            prevFreshOrangeCnt = freshOrangeCnt
            cnt += 1
            for y in range(M):
                for x in range(N):
                    if grid[y][x] == markRottenOrange:
                        grid[y][x] = 0

                        if (y + 1 < M) and (grid[y + 1][x] == 1):
                            grid[y + 1][x] = -markRottenOrange
                            freshOrangeCnt -= 1
                        if (x + 1 < N) and (grid[y][x + 1] == 1):
                            grid[y][x + 1] = -markRottenOrange
                            freshOrangeCnt -= 1
                        if (y - 1 >= 0) and (grid[y - 1][x] == 1):
                            grid[y - 1][x] = -markRottenOrange
                            freshOrangeCnt -= 1
                        if (x - 1 >= 0) and (grid[y][x - 1] == 1):
                            grid[y][x - 1] = -markRottenOrange
                            freshOrangeCnt -= 1

            markRottenOrange = -markRottenOrange

            # for row in grid:
            #     print(*row)
            # print("-----"* 10)


        return cnt
