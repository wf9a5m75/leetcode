class Solution:

    def mining(self, grid: List[List[int]], y: int, x: int, soFarGold: int) -> int:
        if grid[y][x] == 0:
            # If 0 gold cell, stop minining.
            # (Because we can't visit the same cells, even we walked. So we can't go back)
            return soFarGold

        M = len(grid)
        N = len(grid[0])


        # Collect the gold at the current cell
        gold = grid[y][x]
        soFarGold += gold

        # We can't visit the current cell again
        grid[y][x] = 0

        result = soFarGold
        for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nextY = y + delta[0]
            nextX = x + delta[1]
            if (0 <= nextY < M) and (0 <= nextX < N):
                result = max(result, self.mining(grid, nextY, nextX, soFarGold))

        # restore the cell information for next turn
        grid[y][x] = gold

        return result


    def getMaximumGold(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        # We have to start from the cell where is not 0,
        # because we can't visit a cell with 0 gold.
        goldCells = []
        for y in range(M):
            for x in range(N):
                if grid[y][x]:
                    goldCells.append((y, x))

        # Let's collect golds!
        maxGold = 0
        for cellLoc in goldCells:
            maxGold = max(maxGold, self.mining(grid, cellLoc[0], cellLoc[1], 0))
        return maxGold
